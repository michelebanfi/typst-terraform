#import "template.typ" : *

#show: project.with(
  title: {{TITLE}},
  authors: (
    (name: "Author 1", affiliation: ""),
    (name: "Author 2", affiliation: ""),
  ),
  abstract: [],
  date: "",
)