use std::fs::read_to_string;
use std::collections::HashMap;

fn is_num(s: &String) -> bool {
    return match s.parse::<u16>() {
        Ok(_x) => true,
        _ => false
    }
}

fn get_val (s: &String, map: &HashMap<&String, u16>) -> Result<u16, &'static str> {
    return if is_num(s) {
        Ok(s.parse::<u16>().unwrap())
    } else {
        // println!("{}", s);
        match map.get(s) {
            Some(x) => Ok(*x),
            _ => Err("no")
        }
    }
}

fn part1_and_2(commands: &Vec<Vec<String>>, return_wire: &String, b_override: Option<u16>) -> u16 {
    let mut wires: HashMap<&String, u16> = HashMap::new();

    while !wires.contains_key(return_wire) {
        for command in commands {
            if command[0] == "NOT" {
                match get_val(&command[1], &wires) {
                    Ok(x) => wires.insert(&command[3], !x as u16),
                    _ => continue,
                };
            } else if command[1] == "LSHIFT" {
                // println!("LSHIFT");
                let val = get_val(&command[0], &wires);
                let shift_by = get_val(&command[2], &wires);
                match (val, shift_by) {
                    (Ok(x), Ok(y)) => wires.insert(&command[4], x << y),
                    (_, _) => continue,
                };
            } else if command[1] == "RSHIFT" {
                // println!("RSHIFT");
                let val = get_val(&command[0], &wires);
                let shift_by = get_val(&command[2], &wires);
                match (val, shift_by) {
                    (Ok(x), Ok(y)) => wires.insert(&command[4], x >> y),
                    (_, _) => continue,
                };
            } else if command[1] == "AND" {
                // println!("AND");
                let val1 = get_val(&command[0], &wires);
                let val2 = get_val(&command[2], &wires);
                match (val1, val2) {
                    (Ok(x), Ok(y)) => wires.insert(&command[4], x & y),
                    (_, _) => continue,
                };
            } else if command[1] == "OR" {
                // println!("OR");
                let val1 = get_val(&command[0], &wires);
                let val2= get_val(&command[2], &wires);
                match (val1, val2) {
                    (Ok(x), Ok(y)) => wires.insert(&command[4], x | y),
                    (_, _) => continue,
                };
            } else if command[1] == "->" {
                if command[2] == "b" && b_override.is_some() {
                    wires.insert(&command[2], b_override.unwrap() as u16);
                } else {
                    let val = get_val(&command[0], &wires);
                    match val {
                        Ok(x) => wires.insert(&command[2], x as u16),
                        _ => continue,
                    };
                }
            } else {
                panic!("NO a vaild command");
            }
        }
    }
    return *wires.get(return_wire).unwrap()
}

fn read_input(path: &str) -> Vec<Vec<String>> {
    return read_to_string(path)
    .unwrap()
    .split("\n")
    .map(|x|
        x.trim().split(" ").map(|y| y.trim().to_string()).collect::<Vec<String>>()
    )
    .collect::<Vec<_>>();
}

pub fn solve() {
    let example_input = read_input("src/year_2015/day7/example.txt");
    println!("Example: Wire {} is at value {}", "y", part1_and_2(&example_input, &String::from("y"), Option::None));

    let input = read_input("src/year_2015/day7/input.txt");
    let a =  part1_and_2(&input, &String::from("a"), Option::None);
    println!("Example: Wire {} is at value {}", "a", a);

    let new_a = part1_and_2(&input, &String::from("a"), Some(a));
    println!("Example: Wire {} is at value {} after the b override", "new_a", new_a);
}