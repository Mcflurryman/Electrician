---
version: alpha
name: Voltio Editorial
description: Precisión energética con acento eléctrico controlado.
colors:
  primary: "#07111F"
  secondary: "#536277"
  tertiary: "#A3E635"
  neutral: "#F5F8FC"
  surface: "#FFFFFF"
  info: "#06B6D4"
  success: "#15803D"
  warning: "#D97706"
  danger: "#DC2626"
typography:
  h1:
    fontFamily: Geist
    fontSize: 3.5rem
    fontWeight: 750
    lineHeight: 1.05
    letterSpacing: "-0.04em"
  h2:
    fontFamily: Geist
    fontSize: 2.25rem
    fontWeight: 700
    lineHeight: 1.15
    letterSpacing: "-0.025em"
  body-md:
    fontFamily: Inter
    fontSize: 1rem
    fontWeight: 400
    lineHeight: 1.6
  metric:
    fontFamily: JetBrains Mono
    fontSize: 1rem
    fontWeight: 650
    lineHeight: 1.3
rounded:
  sm: 8px
  md: 12px
  lg: 20px
spacing:
  xs: 4px
  sm: 8px
  md: 16px
  lg: 24px
  xl: 32px
  section: 64px
components:
  button-primary:
    backgroundColor: "{colors.tertiary}"
    textColor: "{colors.primary}"
    rounded: "{rounded.sm}"
    padding: 12px
  button-primary-hover:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.surface}"
    rounded: "{rounded.sm}"
    padding: 12px
  card:
    backgroundColor: "{colors.surface}"
    textColor: "{colors.primary}"
    rounded: "{rounded.md}"
    padding: 24px
  section-muted:
    backgroundColor: "{colors.neutral}"
    textColor: "{colors.primary}"
    rounded: "{rounded.lg}"
    padding: 32px
  alert-info:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.info}"
    rounded: "{rounded.sm}"
    padding: 16px
  alert-success:
    backgroundColor: "{colors.success}"
    textColor: "{colors.surface}"
    rounded: "{rounded.sm}"
    padding: 16px
  alert-warning:
    backgroundColor: "{colors.warning}"
    textColor: "{colors.primary}"
    rounded: "{rounded.sm}"
    padding: 16px
  alert-danger:
    backgroundColor: "{colors.danger}"
    textColor: "{colors.surface}"
    rounded: "{rounded.sm}"
    padding: 16px
---

## Overview

Voltio Editorial combina claridad periodística y precisión de ingeniería. La energía aparece como acento y flujo, no como ruido visual.

## Colors

El azul tinta crea confianza y jerarquía. El lima eléctrico se reserva para acciones, foco y métricas decisivas. El cian identifica información técnica. Las superficies claras mantienen legibilidad prolongada.

## Typography

Geist aporta carácter técnico a títulos; Inter optimiza lectura; JetBrains Mono alinea unidades y métricas. Mantener cuerpos amplios, líneas cortas y números tabulares.

## Layout

Contenedor máximo de 1200 px y columna editorial de 760 px. Escala de 4 px, espacio generoso y grids 4/6/12 columnas según viewport.

## Elevation & Depth

Bordes sutiles y sombras mínimas. El contraste de superficies define jerarquía; no usar resplandores detrás de texto.

## Shapes

Radios moderados y consistentes. Líneas de circuito o gradientes lima-cian sólo en hero, separadores y visualizaciones.

## Components

Una acción primaria por bloque. Tarjetas muestran contexto, unidad, fuente y estado desconocido. Tablas conservan semántica y un fallback móvil legible.

## Do's and Don'ts

Usar acento eléctrico con intención, foco visible, movimiento breve y datos claros. No usar estética de casino, neón continuo, urgencia falsa, glassmorphism de bajo contraste ni animaciones sin alternativa reducida.
