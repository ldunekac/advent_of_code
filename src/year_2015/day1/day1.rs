use std::fs;

fn to_num(c: &u8) -> i32 {
    return match *c as char {
        ')' => -1,
        '(' => 1,
        _ => panic!("WAT")
    }
}

fn part1(input: &Vec<u8>) {
    let floor = input.into_iter().map(|x| to_num(x)).reduce(|a, b| a + b).unwrap();
    println!("You are on floor {}", floor);
}

fn part2(input: &Vec<u8>) {
    let mut current_floor = 0;

    for (idx, op) in input.iter().enumerate() {
        current_floor += to_num(&op);
        if current_floor < 0 {
            println!("Entered Basement at position {}", idx + 1);
            break;
        }
    }
}

pub fn solve() {
    let example_input = fs::read_to_string("src/year_2015/day1/example.txt").unwrap().chars().map(|x| x as u8).collect::<Vec<u8>>();
    part1(&example_input);

    let input = fs::read_to_string("src/year_2015/day1/input.txt").unwrap().chars().map(|x| x as u8).collect::<Vec<u8>>();
    part1(&input);

    part2(&example_input);
    part2(&input);
}