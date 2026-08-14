from __future__ import annotations

import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SKILLS = ROOT / ".agents" / "skills"
EXPECTED = {
    "discover-keywords": ["references/keyword-framework.md"],
    "discover-products": ["references/product-selection-framework.md"],
    "research-product": ["references/research-methodology.md"],
    "score-product": ["references/scoring-framework.md"],
    "design-system": [
        "references/visual-guidelines.md",
        "references/component-guidelines.md",
    ],
    "ui-builder": ["references/ui-patterns.md"],
    "create-product-page": ["references/product-page-structure.md"],
    "create-comparison": ["references/comparison-framework.md"],
    "seo-audit": [
        "references/seo-checklist.md",
        "references/technical-seo.md",
    ],
}


def parse_frontmatter(text: str, path: Path) -> dict[str, str]:
    if not text.startswith("---\n"):
        raise ValueError(f"{path}: frontmatter ausente al inicio")
    match = re.match(r"---\n(.*?)\n---\n", text, flags=re.DOTALL)
    if not match:
        raise ValueError(f"{path}: frontmatter sin cierre válido")
    data: dict[str, str] = {}
    for line in match.group(1).splitlines():
        if ":" in line and not line.startswith((" ", "\t")):
            key, value = line.split(":", 1)
            data[key.strip()] = value.strip().strip('"\'')
    if not text[match.end():].strip():
        raise ValueError(f"{path}: cuerpo vacío")
    body = text[match.end():]
    required_sections = {
        "procedimiento": r"^## Procedimiento\s*$",
        "pitfalls": r"^## Pitfalls\s*$",
        "verificación": r"^## (?:Salida y )?[Vv]erificación\s*$",
    }
    for section, pattern in required_sections.items():
        if not re.search(pattern, body, flags=re.MULTILINE):
            raise ValueError(f"{path}: falta la sección {section}")
    return data


def validate_skills(errors: list[str]) -> int:
    checked = 0
    for name, references in EXPECTED.items():
        skill_dir = SKILLS / name
        skill_path = skill_dir / "SKILL.md"
        try:
            text = skill_path.read_text(encoding="utf-8")
            meta = parse_frontmatter(text, skill_path)
            if meta.get("name") != name:
                errors.append(f"{skill_path}: name debe ser {name}")
            description = meta.get("description", "")
            if not description or len(description) > 60 or not description.endswith("."):
                errors.append(
                    f"{skill_path}: description debe existir, terminar en punto y tener <=60 caracteres"
                )
            for reference in references:
                ref_path = skill_dir / reference
                if not ref_path.is_file() or ref_path.stat().st_size == 0:
                    errors.append(f"{ref_path}: referencia ausente o vacía")
            checked += 1
        except (OSError, ValueError) as exc:
            errors.append(str(exc))
    return checked


def validate_json(errors: list[str]) -> int:
    paths = sorted((ROOT / "data").rglob("*.json"))
    documents: dict[str, object] = {}
    for path in paths:
        try:
            documents[path.name] = json.loads(path.read_text(encoding="utf-8"))
        except (OSError, json.JSONDecodeError) as exc:
            errors.append(f"{path}: {exc}")

    try:
        import jsonschema  # type: ignore

        pairs = [
            ("keyword-map.json", "keyword-map.schema.json"),
            ("product-candidates.json", "product-candidates.schema.json"),
        ]
        for document_name, schema_name in pairs:
            jsonschema.validate(documents[document_name], documents[schema_name])
    except ImportError:
        print("AVISO: jsonschema no instalado; sólo se validó sintaxis JSON")
    except Exception as exc:  # jsonschema expone varias clases según versión
        errors.append(f"Validación JSON Schema: {exc}")
    return len(paths)


def main() -> int:
    errors: list[str] = []
    skill_count = validate_skills(errors)
    json_count = validate_json(errors)
    if errors:
        print("VALIDACIÓN FALLIDA")
        for error in errors:
            print(f"- {error}")
        return 1
    print(f"OK: {skill_count} skills y {json_count} archivos JSON validados")
    return 0


if __name__ == "__main__":
    sys.exit(main())
