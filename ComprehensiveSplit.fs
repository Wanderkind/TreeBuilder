open System
let csplit = fun (s: string) -> s.Split([|' '; '\t'|], System.StringSplitOptions.RemoveEmptyEntries)
