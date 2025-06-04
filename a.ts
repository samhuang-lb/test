/**
 * Concat 工具类型：将 n 个数组类型连接成一个单一的数组类型。
 *
 * @template Arrays - 一个由多个数组类型组成的元组（tuple）。
 *                    例如：`[[1, 2], ['a', 'b'], [true]]`
 */
type Concat<Arrays extends unknown[][]> =
  Arrays extends [
    infer Head extends unknown[], // 推断出第一个数组（Head）
    ...infer Tail extends unknown[][] // 推断出剩余的数组（Tail），Tail 也是一个数组的数组
  ]
  ? [...Head, ...Concat<Tail>] // 将 Head 展开，并递归调用 ConcatN 处理 Tail，然后连接两者
  : []; 
type ConcatDemo=Concat<[[1,2,3,4],[{a:1}]]>

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

type PartialUser = DeepPartial<User>;



import { faker } from '@faker-js/faker';

const randomName = faker.person.fullName(); // Rowan Nikolaus
const randomEmail = faker.internet.email(); // Kassandra.Haley@erich.biz
console.log(randomName,randomEmail);
