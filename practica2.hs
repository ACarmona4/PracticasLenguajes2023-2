import Data.Char (digitToInt, isDigit)

convertirInt::String->[Int]
convertirInt = map digitToInt . filter isDigit

sumaMultiplicacion::[Int] -> Int
sumaMultiplicacion lista = sum (zipWith (*) lista [10,9..1])

moduloOnce :: Int -> Bool
moduloOnce numero = numero `mod` 11 == 0

verificarISBN::String->Bool
verificarISBN = moduloOnce . sumaMultiplicacion . convertirInt