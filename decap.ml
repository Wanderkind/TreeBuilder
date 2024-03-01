let decap f lst = f (List.hd lst) (List.tl lst)
;;

(*
exapmle:
https://www.acmicpc.net/source/share/087f3a5c00594d13858777aadac80b4d
*)

(*
for F#:
let decap f lst = f (List.head lst) (List.tail lst)
;;
*)
