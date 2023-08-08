use std::fs;
use std::cmp;

#[derive(Debug)]
struct Dims {
    length: u128,
    width: u128,
    height: u128,
}

impl Dims {
    fn area_top(&self) -> u128 {
        return self.height * self.length
    }

    fn area_side(&self) -> u128 {
        return self.width * self.height
    }

    fn area_front(&self) -> u128 {
        return self.length * self.width
    }

    fn surface_area(&self) -> u128 {
        return 2 * (self.area_top() + self.area_side() + self.area_front())
    }

    fn min_surface_area(&self) -> u128 {
        return cmp::min( cmp::min(self.area_top(), self.area_side()), self.area_front())
    }

    fn volume(&self) -> u128 {
        return self.width * self.height * self.length
    }

    fn smallest_perimeter(&self) -> u128 {
        let side1 = 2 * self.length;
        let side2 = 2 * self.height;
        let side3 = 2 * self.width;
        return  cmp::min(cmp::min(side1.clone() + side2.clone(), side2 + side3.clone()), side3 + side1);
    }
}

fn to_dims(box_string: &str) -> Dims {
    let box_values = box_string.trim().split("x").map(|x| x.parse::<u128>().unwrap()).collect::<Vec<u128>>();
    return Dims{
        length: *box_values.get(0).unwrap(),
        width: *box_values.get(1).unwrap(),
        height: *box_values.get(2).unwrap(),
    }
}

fn read_input(path: &str) -> Vec<Dims> {
    return fs::read_to_string(path).unwrap().split("\n").map(|x| to_dims(x)).collect::<Vec<Dims>>();
}

fn part1(packages: &Vec<Dims>) -> u128 {
    return packages.iter().map(|x| x.surface_area() + x.min_surface_area()).reduce(|x, y| x + y).unwrap();
}

fn part2(packages: &Vec<Dims>) -> u128 {
    return packages.iter().map(|x| x.smallest_perimeter() + x.volume()).reduce(|x, y| x + y).unwrap();
}

pub fn solve() {
    let example_input = read_input("src/year_2015/day2/example.txt");
    println!("Need {} square feet of paper", part1(&example_input));

    let input =  read_input("src/year_2015/day2/input.txt");
    println!("Need {} square feet of paper", part1(&input));

    println!("Total ribbon needed is {}", part2(&example_input));
    println!("Total ribbon needed is {}", part2(&input));
}