use std::collections::HashMap;
use std::fs;

#[derive(Clone, Debug, Eq, Hash)]
struct Location {
    x: i128,
    y: i128
}

impl PartialEq for Location {
    fn eq(&self, other: &Self) -> bool {
        self.x == other.x && self.y == other.y
    }
}


fn to_direction(c: &char) -> u8 {
    match c {
        '^' => 1,
        '>' => 2,
        'v' => 3,
        '<' => 4,
        _ => panic!("WAT")
    }
}

fn read_input(path: &str) -> Vec<u8> {
    return fs::read_to_string(path).unwrap().chars().map(|x| x as u8).collect()
}

fn get_locations(directions: &Vec<u8>) -> HashMap<Location, u128> {
    let mut current_location = Location{x: 0, y:0};
    let mut visited: HashMap<Location, u128> = std::collections::HashMap::from([(current_location.clone(), 1)]);

    for direction in directions {
        match *direction as char {
            '^' => current_location.y += 1,
            '>' => current_location.x += 1,
            'v' => current_location.y -= 1,
            '<' => current_location.x -= 1,
            _ => panic!("WAT")
        }
        match visited.get(&current_location) {
            Some(x) => visited.insert(current_location.clone(), x + 1),
            _ => visited.insert(current_location.clone(), 1)
        };
    }
    return  visited;
}

fn part1(directions: &Vec<u8>) -> u128 {
    return  get_locations(directions).len() as u128;
}

fn part2(directions: &Vec<u8>) -> u128 {
    let santa: Vec<u8> = directions.into_iter().enumerate().filter(|&i| i.0 % 2 == 0).map(|x| *x.1).collect::<Vec<u8>>();
    let robot: Vec<u8> = directions.into_iter().enumerate().filter(|&i| (i.0 + 1) % 2 == 0).map(|x| *x.1).collect::<Vec<u8>>();

    let mut santa_houses = get_locations(&santa);
    let robot_houses = get_locations(&robot);
    santa_houses.extend(robot_houses);
    return santa_houses.len() as u128
}

pub fn solve() {
    let example_input = read_input("src/year_2015/day3/example.txt");
    println!("Total number of houses that received at least one gift is {}", part1(&example_input));

    let input = read_input("src/year_2015/day3/input.txt");
    println!("Total number of houses that received at least one gift is {}", part1(&input));

    println!("Total number of houses that received at least one gift with help is {}", part2(&example_input));
    println!("Total number of houses that received at least one gift with help is {}", part2(&input));
}