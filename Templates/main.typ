#import "template.typ": *
#import "@preview/quill:0.2.0": *

#show: project.with(
  title: {{PROJECT_NAME}},
  authors: (
    {{AUTHOR}},
  ),
)

#outline(
  indent: auto
)

// #set math.equation(numbering: "(1)")

#include "Chapters/1.typ"
#include "Chapters/2.typ"
#include "Chapters/3.typ"
#include "Chapters/4.typ"