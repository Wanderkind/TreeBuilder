let isqrt x =
    let rec f w =
        if w > x then w
        else 4L*w |> f
    let rec g z r p =
        if p <= 1L then r
        else
            let p4 = p/4L
            let t, r2 = z - r - p4, r/2L
            if t < 0 then g z r2 p4
            else g t (r2 + p4) p4
    f 1L |> g x 0L

(*
for i = 0 to 101 do
    printfn "%d: %d" i (i |> int64 |> isqrt)
done
*)
