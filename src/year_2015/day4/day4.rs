fn hash_that_starts_with(key: &str, starts: &str) -> usize {
    let max_num: usize = 200000000;
    for i in 0..max_num {
        let ans = format!("{}{}", key, i);
        let md5_hash = md5::compute(ans);
        if format!("{:x}", md5_hash).starts_with(starts) {
            return i as usize
        }
    }
    return 0;
}

fn part1(key: &str) -> usize {
    return hash_that_starts_with(key, "00000");
}

fn part2(key: &str) -> usize {
    return hash_that_starts_with(key, "000000");
}

pub fn solve() {
    println!("Number to make md5 hash start with 5 zeros is {}", part1(&"abcdef"));
    println!("Number to make md5 hash start with 5 zeros is {}", part1(&"pqrstuv"));
    println!("Number to make md5 hash start with 5 zeros is {}", part1(&"bgvyzdsv"));

    println!("Number to make md5 hash start with 6 zeros is {}", part2(&"bgvyzdsv"));
}