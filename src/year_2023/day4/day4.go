package day4

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
	"strings"
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

type Game struct {
	card int
	winning []int
	guesses []int
}

type Stats struct {
	cardNum int
	NumCopies int
	cardScore int
}

func parse_input(lines []string) (games []Game) {

	for _, line := range lines {
		tmp := strings.Split(line, ":")
		card, _ := strconv.Atoi(strings.Split(tmp[0], " ")[1])
		values := strings.Split(tmp[1], "|")
		winning_row := strings.TrimSpace(values[0])
		guesses_row := strings.TrimSpace(values[1])

		var winning_nums []int
		for _, numStr := range strings.Split(winning_row, " ") {
			num, err := strconv.Atoi(numStr); if err == nil {
				winning_nums = append(winning_nums, num)
			}
		}

		var guesses_nums []int
		for _, numStr := range strings.Split(guesses_row, " ") {
			num, err := strconv.Atoi(numStr); if err == nil {
				guesses_nums = append(guesses_nums, num)
			}
		}

		games = append(games, Game{card, winning_nums, guesses_nums})
	}
	return
}

func part1(lines []string) (total int) {
	games := parse_input(lines)

	for _, game := range games {
		num_matches := 0
		for _, win := range game.winning {
			for _, guess := range game.guesses {
				if win == guess {
						num_matches += 1
					}
				}
			}
		if num_matches > 0 {
			score := 1 << (num_matches - 1)
			total += score
		}
	}
	return
}

func initialize_score(games []Game) (stats []Stats) {
	for _, game := range games {
		stats = append(stats, Stats{game.card, 1, 0})
	}
	return
}

func part2(lines []string) (total int) {
	games := parse_input(lines)
	stats := initialize_score(games)

	for idx, game := range games {
		num_matches := 0
		for _, win := range game.winning {
			for _, guess := range game.guesses {
				if win == guess {
					num_matches += 1
				}
			}
		}
		if num_matches > 0 {
			score := 1 << (num_matches - 1)
			current := stats[idx]
			stats[idx] = Stats{current.cardNum, current.NumCopies, score}
			for i := 1; i <= num_matches; i++ {
				if idx+i < len(games) {
					next := stats[idx+i]
					stats[idx+i] = Stats{next.cardNum, next.NumCopies + current.NumCopies, next.cardScore}
				}
			}
		}
	}

	for _, stat := range stats{
		total += stat.NumCopies
	}
	return
}

func Solve() {

	input, _ := get_lines("src/year_2023/day4/example.txt")
	ans := part1(input)
	fmt.Println("Part 1 example answer is ", ans)

	input, _ = get_lines("src/year_2023/day4/input.txt")
	ans = part1(input)
	fmt.Println("Part 1 input answer is ", ans)
	fmt.Println("")


	input, _ = get_lines("src/year_2023/day4/example.txt")
	ans = part2(input)
	fmt.Println("Part 2 example answer is ", ans)

	input, _ = get_lines("src/year_2023/day4/input.txt")
	ans = part2(input)
	fmt.Println("Part 2 input answer is ", ans)

}