type Concat<T extends any[], U extends any[]> = [...T, ...U];
type Tuple1 = [1, 2];
type Tuple2 = [3, 4];
type MergedTuple = Concat<Tuple1, Tuple2>; //  [1, 2, 3, 4]
type OOO={
    a?:number
    b:string
}
type xx=NonNullable<OOO['a']>

type DeepPartial<T> = {
    [K in keyof T]?: T[K] extends object ? DeepPartial<T[K]> : T[K];
};

// 示例
interface User {
    id: number;
    name: string;
    address: {
        city: string;
        zip: number;
    };
    hobbies: string[];
};

// 使用 DeepPartial
type PartialUser = DeepPartial<User>;

// 测试
const user4: PartialUser = {
    id: 1,
    address: {
        zip: 10001, // 只提供嵌套对象的部分属性
    },
};