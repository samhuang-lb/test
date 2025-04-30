type First<T extends any[]> = T extends [infer FirstElement, ...any[]] ? FirstElement : never;
type Tuple = [5, 6, 7];
type FirstElement = First<Tuple>; //  5