type Concat<T extends any[], U extends any[]> = [...T, ...U];
type Tuple1 = [1, 2];
type Tuple2 = [3, 4];
type MergedTuple = Concat<Tuple1, Tuple2>; //  [1, 2, 3, 4]