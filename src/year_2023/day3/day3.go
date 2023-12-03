package day3

import (
	"bufio"
	"fmt"
	"os"
	"strings"
	"strconv"
)


func get_lines(fileName string) (fileLines []string, err error) {

	readFile, err := os.Open(fileName)

	if err != nil {
		return
	}

	fileScanner := bufio.NewScanner(readFile)
	fileScanner.Split(bufio.ScanLines)

	for fileScanner.Scan() {
		fileLines = append(fileLines, fileScanner.Text())
	}

	readFile.Close()

	return
}

func parse_input(lines []string) (grid []string) {
	// numRows := len(lines)
	numCol := len(lines[0])
	butter := strings.Repeat(".", numCol+2)

	grid = append(grid, butter)
	for _, line := range lines {
		line = "." + line + "."
		grid = append(grid, line)
	}
	grid = append(grid, butter)
	return grid
}


func haveSpecial(input rune) bool {
	allowed := []rune{'!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-', '_', '+', '=', '/'}
	for _, c := range allowed {
		if c == input {
			return true
		}
	}
	return false
}

func isGear(input rune) bool {
	allowed := []rune{'!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-', '_', '+', '=', '/'}
	for _, c := range allowed {
		if c == input {
			return true
		}
	}
	return false
}

func symbol_around(i int, j int, grid []string) bool {
	return haveSpecial(rune(grid[i-1][j-1])) ||
	haveSpecial(rune(grid[i-1][j])) ||
	haveSpecial(rune(grid[i-1][j+1])) ||
	haveSpecial(rune(grid[i][j-1])) ||
	haveSpecial(rune(grid[i][j+1])) ||
	haveSpecial(rune(grid[i+1][j-1])) ||
	haveSpecial(rune(grid[i+1][j])) ||
	haveSpecial(rune(grid[i+1][j+1])) 
}

func gear_around(i int, j int, grid []string) (int, int, bool) {
	if isGear(rune(grid[i-1][j-1])) {
		return i-1, j-1, true
	} else if isGear(rune(grid[i-1][j])) {
		return i-1, j, true
	} else if isGear(rune(grid[i-1][j+1])) {
		return i-1, j+1, true
	} else if isGear(rune(grid[i][j-1])) {
		return i, j-1, true
	} else if isGear(rune(grid[i][j+1])) {
		return i, j+1, true
	} else if isGear(rune(grid[i+1][j-1])) {
		return i+1, j-1, true
	} else if isGear(rune(grid[i+1][j])) {
		return i+1, j, true
	} else if isGear(rune(grid[i+1][j+1])) {
		return i+1, j+1, true
	} else {
		return 0, 0, false
	}
}

func part1(lines []string) (total int) {
	grid := parse_input(lines)
	total = 0
	for i := 1; i < len(grid) - 1; i += 1 {
		row := grid[i]
		str_num := ""
		has_symbol := false
		for j := 1; j < len(row) - 1; j += 1 {
			c := string(row[j])
			if _, err := strconv.Atoi(c); err == nil {
				str_num = str_num + c
				has_symbol = has_symbol || symbol_around(i, j, grid)
			} else {
				if len(str_num) > 0 && has_symbol{
					num_to_add, _ :=  strconv.Atoi(str_num)
					total = total + num_to_add
					str_num = ""
					has_symbol = false
				} else {
					// if len(str_num) > 0 {
					// 	fmt.Println("Not " + str_num)
					// }
					has_symbol = false
					str_num = ""
				}
			}
		}
		if len(str_num) > 0 && has_symbol {
			num_to_add, _ :=  strconv.Atoi(str_num)
			total = total + num_to_add
		}
	}
	return
}

type ij struct {
	i, j int
}

func part2(lines []string) (total int) {
	grid := parse_input(lines)
	total = 0
	
	gearMap := make(map[ij][]int)
	var gearLoc ij
	for i := 1; i < len(grid) - 1; i += 1 {
		row := grid[i]
		str_num := ""
		has_symbol := false
		for j := 1; j < len(row) - 1; j += 1 {
			c := string(row[j])
			if _, err := strconv.Atoi(c); err == nil {
				str_num = str_num + c
				gi, gj, has_gear := gear_around(i, j, grid)
				has_symbol = has_symbol || has_gear
				if has_gear {
					gearLoc = ij{gi, gj}
				}
			} else {
				if len(str_num) > 0 && has_symbol{
					num_to_add, _ :=  strconv.Atoi(str_num)
					gearMap[gearLoc] = append(gearMap[gearLoc], num_to_add)

					str_num = ""
					has_symbol = false
				} else {
					gearLoc = ij{0,0}
					has_symbol = false
					str_num = ""
				}
			}
		}
		if len(str_num) > 0 && has_symbol {
			num_to_add, _ :=  strconv.Atoi(str_num)
			gearMap[gearLoc] = append(gearMap[gearLoc], num_to_add)
		}
	}

	for _, ratios := range gearMap {
		if len(ratios) == 2 {
			total += ratios[0] * ratios[1]
		}
	}
	return
}

func Solve() {

	input, _ := get_lines("src/year_2023/day3/example.txt")
	ans := part1(input)
	fmt.Println("Part 1 example answer is ", ans)

	input, _ = get_lines("src/year_2023/day3/input.txt")
	ans = part1(input)
	fmt.Println("Part 1 input answer is ", ans)
	fmt.Println("")


	input, _ = get_lines("src/year_2023/day3/example.txt")
	ans = part2(input)
	fmt.Println("Part 2 example answer is ", ans)

	input, _ = get_lines("src/year_2023/day3/input.txt")
	ans = part2(input)
	fmt.Println("Part 2 input answer is ", ans)

}