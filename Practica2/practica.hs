verificarDigito :: Char -> Bool
verificarDigito c = c >= '0' && (c <= '9' || c == 'x' || c == 'X')

charToInt :: Char -> Int
charToInt c = if (c == 'x' || c == 'X') then 10 else (fromEnum c - fromEnum '0')

convertirInt :: String -> [Int]
convertirInt = map charToInt . filter verificarDigito

sumaMultiplicacion :: [Int] -> Int
sumaMultiplicacion lista = sum (zipWith (*) lista [10,9..1])

moduloOnce :: Int -> Bool
moduloOnce numero = numero `mod` 11 == 0

verificarISBN :: String -> Bool
verificarISBN = moduloOnce . sumaMultiplicacion . convertirInt