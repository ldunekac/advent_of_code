use std::fs::read_to_string;

enum Op {
    On,
    Off,
    Toggle
}

fn pasre_coord(coord: &str) -> (usize, usize) {
    let mut iter = coord.split(",").map(|x| x.trim().parse::<usize>().expect("NOOOO")).collect::<Vec<usize>>().into_iter();
    return (iter.next().unwrap(), iter.next().unwrap());
}

fn parse_instruction(instruction: &str) -> (Op, (usize, usize), (usize, usize)){
    let tokens = instruction.split(" ").collect::<Vec<&str>>();
    return match [tokens[0], tokens[1]] {
        ["turn", "on"] => (Op::On, pasre_coord(tokens.get(2).unwrap()), pasre_coord(tokens.get(4).unwrap())),
        ["turn", "off"] => (Op::Off, pasre_coord(tokens.get(2).unwrap()), pasre_coord(tokens.get(4).unwrap())),
        ["toggle", _] => (Op::Toggle, pasre_coord(tokens.get(1).unwrap()), pasre_coord(tokens.get(3).unwrap())),
        _ => panic!("WAT")
    }
}

fn part1(instructions: &Vec<String>) -> usize {
    let mut grid = vec![[0 as u8; 1000]; 1000];

    for instruction in instructions {
        let (op, (start_x, start_y), (end_x, end_y)) = parse_instruction(instruction);
        for i in start_x..end_x+1 {
            for j in start_y..end_y+1 {
                match op {
                    Op::On => grid[i][j] = 1,
                    Op::Off => grid[i][j] = 0,
                    Op::Toggle => grid[i][j] = (grid[i][j] + 1) % 2
                }
            }
        }
    }

    let mut total: usize = 0;
    for row in grid {
        for val in row {
            total += val as usize
        }
    }
    return total;
}

fn part2(instructions: &Vec<String>) -> usize {
    let mut grid = vec![[0 as u8; 1000]; 1000];

    for instruction in instructions {
        let (op, (start_x, start_y), (end_x, end_y)) = parse_instruction(instruction);
        for i in start_x..end_x+1 {
            for j in start_y..end_y+1 {
                match op {
                    Op::On => grid[i][j] += 1,
                    Op::Off => grid[i][j] = if grid[i][j] == 0 { 0 } else {grid[i][j] -1},
                    Op::Toggle => grid[i][j] += 2,
                }
            }
        }
    }

    let mut total: usize = 0;
    for row in grid {
        for val in row {
            total += val as usize
        }
    }
    return total;
}

fn read_input(path: &str) -> Vec<String>{
    return read_to_string(path).unwrap().split("\n").map(|x| x.to_string()).collect::<Vec<String>>();
}

pub fn solve() {
    let example_input = read_input("src/year_2015/day6/example.txt");
    println!("{:?}", example_input);
    println!("Example: Total number of lights on are {}", part1(&example_input));

    let input = read_input("src/year_2015/day6/input.txt");
    println!("Input: Total number of lights on are {}", part1(&input));

    println!("Input: Total intensity of lights on are {}", part2(&input));
}