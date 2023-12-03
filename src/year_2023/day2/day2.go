package day2

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
	"strings"
)

type round struct {
	red int
	green int
	blue int
}

type game struct {
	id int
	rounds []round
}

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

func parse_input(lines []string) (games []game) {
	for _, line := range lines {
		gameInfo := strings.Split(line, ":")
		gameNumber, _ := strconv.Atoi(gameInfo[0][5:])
		//fmt.Println("Game ", gameNumber)
		rounds := strings.Split(gameInfo[1], ";")

		var gameRounds []round
		for _, r := range rounds {
			marbles := strings.Split(r, ",")
			red, green, blue := 0, 0, 0
			for _, marble := range marbles {
				pair := strings.Split(strings.TrimSpace(marble), " ")
				marbleCount, _ := strconv.Atoi(pair[0])
				marbleColor := strings.TrimSpace(pair[1])
				//fmt.Println("Marble color", marbleColor)
				if marbleColor == "red" {
					red = marbleCount
				} else if marbleColor == "green" {
					green = marbleCount
				} else if marbleColor == "blue" {
					blue = marbleCount
				}
			}
			gameRound := round{red, green, blue}
			gameRounds = append(gameRounds, gameRound)
		}
		games = append(games, game{gameNumber, gameRounds})
	}
	return
}


func part2 (lines []string) (total int) {
	games := parse_input(lines)

	for _, g := range games {
		redNeeded, greenNeeded, blueNeeded := 0, 0, 0
		for _, r := range g.rounds {
			redNeeded = max(r.red, redNeeded)
			greenNeeded = max(r.green, greenNeeded)
			blueNeeded = max(r.blue, blueNeeded)
		}
		power := redNeeded * greenNeeded * blueNeeded
		total = total + power
	}
	return
}

func part1(lines []string) int {
	games := parse_input(lines)

	redMax, greenMax, blueMax := 12, 13, 14

	total := 0

	for _, g := range games {
		passed := true
		for _, r := range g.rounds {
			if r.red > redMax || r.green > greenMax || r.blue > blueMax {
				//fmt.Println("Game ", g.id, " failed")
				passed = false
				break
			}
		}
		if passed {
		total = total + g.id
		}
	}

	return total
}

func Solve() {

	input, err := get_lines("src/year_2023/day2/example.txt")
	if err != nil {
		fmt.Println("Could not parse input", err)
		return
	}
	ans := part1(input)
	fmt.Println("Part 1 example answer is ", ans)


	input, err = get_lines("src/year_2023/day2/input.txt")
	if err != nil {
		fmt.Println("Could not parse input", err)
		return
	}
	ans = part1(input)
	fmt.Println("Part 1 input answer is ", ans)
	fmt.Println("")


	input, err = get_lines("src/year_2023/day2/example.txt")
	if err != nil {
		fmt.Println("Could not parse input", err)
		return
	}
	ans = part2(input)
	fmt.Println("Part 2 example answer is ", ans)

	input, err = get_lines("src/year_2023/day2/input.txt")
	if err != nil {
		fmt.Println("Could not parse input", err)
		return
	}
	ans = part2(input)
	fmt.Println("Part 2 input answer is ", ans)

}