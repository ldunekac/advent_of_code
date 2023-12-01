package day1

import (
	"fmt"
	"bufio"
	"os"
	"strconv"
	"strings"
)

func parse_input(fileName string) (fileLines []string, err error) {

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

func isNumeric(s string) bool {
    _, err := strconv.Atoi(s)
    return err == nil
}

type Conv struct {
	str string
	digit string
}

func part2(lines []string) int {
	digits := []Conv {Conv{"one", "one1one"},
					  Conv{"two", "two2two"}, 
					  Conv{"three", "three3three"}, 
					  Conv{"four", "four4four"}, 
					  Conv{"five", "five5five"},
					  Conv{"six", "six6six"}, 
					  Conv{"seven", "seven7seven"},
					  Conv{"eight", "eight8eight"},
					  Conv{"nine", "nine9nine"}}
	var newLines []string

	for _, line := range lines {
		for _, wat := range digits {
			line = strings.Replace(line, wat.str, wat.digit, -1)
		}
		newLines = append(newLines, line)
	}
	return part1(newLines)
}

func part1(lines []string) int {

	total := 0
	for _, element := range lines {
		first := ""
		last := ""
		for _, c := range element {
			if isNumeric(string(c)) {
				if first == "" {
					first = string(c)
				}
				last = string(c)
			}
		}
		num, err := strconv.Atoi(first + last)
		if err != nil {
			fmt.Println("Error in converting first + last. Stopping")
			return 0
		} 
		total = total + num
	}
	return total
}

func Solve() {

	input, err := parse_input("src/year_2023/day1/example.txt")
	if err != nil {
		fmt.Println("Could not parse input", err)
		return
	}
	ans := part1(input)
	fmt.Println("Part 1 example answer is ", ans)


	input, err = parse_input("src/year_2023/day1/input.txt")
	if err != nil {
		fmt.Println("Could not parse input", err)
		return
	}
	ans = part1(input)
	fmt.Println("Part 1 input answer is ", ans)
	fmt.Println("")


	input, err = parse_input("src/year_2023/day1/example2.txt")
	if err != nil {
		fmt.Println("Could not parse input", err)
		return
	}
	ans = part2(input)
	fmt.Println("Part 2 example answer is ", ans)

	input, err = parse_input("src/year_2023/day1/input.txt")
	if err != nil {
		fmt.Println("Could not parse input", err)
		return
	}
	ans = part2(input)
	fmt.Println("Part 2 input answer is ", ans)

}