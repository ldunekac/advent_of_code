use std::fs::read_to_string;

fn read_input(path: &str) -> Vec<String>{
    return read_to_string(path).unwrap().split("\n").map(|x| x.trim().to_string()).collect::<Vec<String>>();
}

fn part1(strings: &Vec<String>) -> usize {
    let total_string_len: usize = strings.iter().map(|x| x.len()).sum();

    let mut total_bytes: usize = 0;
    for string in strings {
        let chars = string.as_bytes();
        let mut i = 0;
        let mut bytes_in_str = 0;
        while i < chars.len() {
            let c0 = chars[i] as char;
            if c0 == '"' {
            } else if c0 == '\\' && chars[i + 1] as char == 'x' {
                i += 3;
                bytes_in_str += 1;
            } else if c0 == '\\' {
                i += 1;
                bytes_in_str += 1;
            } else {
                bytes_in_str += 1;
            }
            i += 1;
        }
        total_bytes += bytes_in_str
    }
    return total_string_len - total_bytes
}



fn part2(strings: &Vec<String>) -> usize {
    let total_string_len_org: usize = strings.iter().map(|x| x.len()).sum();

    let mut total_string_len: usize = 0;
    for string in strings {
        total_string_len += string.len() + 2;
        let chars = string.as_bytes();
        let mut i = 0;
        while i < chars.len() {
            let c0 = chars[i] as char;
            if c0 == '"' {
                total_string_len += 1;
            } else if c0 == '\\' && chars[i + 1] as char == 'x' {
                i += 3;
                total_string_len += 1;
            } else if c0 == '\\' {
                i += 1;
                total_string_len += 2;
            } 
            i += 1;
        }
    }
    return total_string_len - total_string_len_org;
}

pub fn solve() {
    let example_input = read_input("src/year_2015/day8/example.txt");
    println!("Example: Memory vs string len {}", part1(&example_input));

    let input = read_input("src/year_2015/day8/input.txt");
    println!("Input: Memory vs string len {}", part1(&input));

    println!("Example 2: Memory vs string len {}", part2(&example_input));
    println!("Input 2: Memory vs string len {}", part2(&input));

}