use std::fs;

fn read_input(path: &str) -> Vec<String>{
    return  fs::read_to_string(path).unwrap().split("\n").map(|x| x.to_string()).collect::<Vec<String>>();
}

fn has_3_vowels(string: &str) -> bool{
    let mut i: u32 = 0;
    for c in string.chars() {
        match c {
            'a' | 'e' | 'i' | 'o' | 'u' => i += 1,
            _ => (),
        }
    }
    return i >= 3;
}

fn twice(string: &str) -> bool {
    let mut prev_c = '0'; // just not a letter
    for c in string.chars() {
        if c == prev_c {
            return true
        }
        prev_c = c
    }
    return false
}

fn not_special(string: &str) -> bool {
    let bad_combos = vec!["ab", "cd", "pq", "xy"];
    return !bad_combos.iter().map(|&x|string.contains(x)).reduce(|x, y| x || y).unwrap();
}

fn twice_pair(string: &str) -> bool {
    for i in 2..string.len() {
        match string[i..].find(&string[i-2..i]) {
            Some(_x) => return true,
            _ => continue
        }
    }
    return false
}

fn repeat_in_between(string: &str) -> bool {
    let chars = string.as_bytes();
    for i in 3..chars.len() {
        if chars.get(i-2).unwrap() == chars.get(i).unwrap() {
            return true;
        }
    }
    return false
}


fn part1(strings: &Vec<String>) -> usize {
    return strings
        .iter()
        .map(|x| has_3_vowels(x) && twice(x) && not_special(x))
        .filter(|&x| x)
        .count();
}

fn part2(strings: &Vec<String>) -> usize {
    return  strings
        .iter()
        .map(|x| twice_pair(x) && repeat_in_between(x))
        .filter(|&x| x)
        .count();
}

pub fn solve() {
    let example_input = read_input("src/year_2015/day5/example.txt");
    println!("Total number of nice strings are {}", part1(&example_input));

    let input = read_input("src/year_2015/day5/input.txt");
    println!("Total number of nice strings are {}", part1(&input));

    let example_input2 = read_input("src/year_2015/day5/example2.txt");
    println!("Total number of nice strings are {}", part2(&example_input2));

    println!("Total number of nice strings are {}", part2(&input));
}