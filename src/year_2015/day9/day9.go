package day9

import (
	"bufio"
	"fmt"
	"math"
	"os"
	"path/filepath"
	"strconv"
	"strings"
)

// Tried a fancy algorithm that did not work out as I wanted so I pivioted.
// There is much extra code since I just wanted to finish the project.

type Crow struct {
	city1  string
	city2  string
	distance  int
}

func readInput(path string) []Crow {
	var savior []Crow
	examplePath, err := filepath.Abs(path)
	if err != nil {
		fmt.Println("No absolute path of " + examplePath)
		return savior
	}

	file, err := os.Open(path)

	if err != nil {
		fmt.Println("Cannot read file " + path)
		return savior
	}

	scanner := bufio.NewScanner(file)

	scanner.Split(bufio.ScanLines)

	var murder []Crow

	for scanner.Scan() {
		splits := strings.Split(scanner.Text(), " ")
		distance, err := strconv.Atoi(splits[4])
		if err != nil {
			fmt.Println("Cannot parse int ", splits[4])
			return savior
		}
		murder = append(murder, Crow{city1: splits[0], city2: splits[2], distance: distance})
	}
	return murder
}

func findShortestPath(murder []Crow) int {
	return findPath(murder, true)
}

func findLongestPath(murder []Crow) int {
	return findPath(murder, false)
}

type Path struct {
	spot int
	totalDistance int
	seen map[int] bool
}

func copyMap[K , V comparable](m map[K]V) map[K]V{
	result := make(map[K]V)
	for k, v := range m {
		result[k] = v
	}
	return result
}
func shortestPath(start int, totalCities int, distMatrix [][]int) int {
	seen := make(map[int] bool)
	seen[start] = true

	var queue []Path
	queue = append(queue, Path{spot: start, totalDistance: 0, seen: seen})
	minDist := int(^uint(0) >> 1)
	for len(queue) > 0 {
		current := queue[0]
		queue = queue[1:]
		if len(current.seen) == totalCities {
			if current.totalDistance < minDist {
				minDist = current.totalDistance
			}
			continue
		}
		for i := 0; i < totalCities; i++ {
			if _, ok := current.seen[i]; !ok {
				totalDistance := current.totalDistance + distMatrix[i][current.spot]
				//fmt.Println(totalDistance)
				seen1 := copyMap(current.seen)
				seen1[i] = true
				queue = append(queue, Path{spot: i, totalDistance: totalDistance, seen: seen1})
			}
		}
	}

	return minDist
}
func longestPath(start int, totalCities int, distMatrix [][]int) int {
	seen := make(map[int] bool)
	seen[start] = true

	var queue []Path
	queue = append(queue, Path{spot: start, totalDistance: 0, seen: seen})
	maxDist := 0
	for len(queue) > 0 {
		current := queue[0]
		queue = queue[1:]
		if len(current.seen) == totalCities {
			if current.totalDistance > maxDist {
				maxDist = current.totalDistance
			}
			continue
		}
		for i := 0; i < totalCities; i++ {
			if _, ok := current.seen[i]; !ok {
				totalDistance := current.totalDistance + distMatrix[i][current.spot]
				seen1 := copyMap(current.seen)
				seen1[i] = true
				queue = append(queue, Path{spot: i, totalDistance: totalDistance, seen: seen1})
			}
		}
	}

	return maxDist
}

func findPath(murder []Crow, smallestPath bool) int {

	var cities = make(map[string]bool)
	for _, crow := range murder {
		cities[crow.city1] = true
		cities[crow.city2] = true
	}
	totalCities := int(math.Ceil(math.Sqrt(2 * float64(len(murder)))))
	cityIndex := make(map[string]int, totalCities)
	i := 0
	for key := range cities {
		cityIndex[key] = i
		i++
	}
	matrix := make([][]int, totalCities)
	for k := 0; k < totalCities; k++ {
		matrix[k] = make([]int, totalCities, totalCities)
	}
	for _, crow := range murder {
		k := cityIndex[crow.city1]
		j := cityIndex[crow.city2]
		matrix[k][j] = crow.distance
		matrix[j][k] = crow.distance
	}

	var pathLen int
	if smallestPath {
		pathLen = int(^uint(0) >> 1)
		for w := 0; w < totalCities; w++ {
			dist := shortestPath(w, totalCities, matrix)
			if dist < pathLen {
				pathLen = dist
			}
		}
	}else {
		pathLen = 0
		for w := 0; w < totalCities; w++ {
			dist := longestPath(w, totalCities, matrix)
			if dist >pathLen {
				pathLen = dist
			}
		}
	}
	return pathLen
}


func part1() {
	fmt.Println("PART 1")
	murder := readInput("src/year_2015/day9/example.txt")
	shortestPath := findShortestPath(murder)
	fmt.Println("The shortest path is ", shortestPath)


	murder2 := readInput("src/year_2015/day9/input.txt")
	shortestPath2 := findShortestPath(murder2)
	fmt.Println("The shortest path is ", shortestPath2)
}

func part2() {
	fmt.Println("PART 2")
	murder := readInput("src/year_2015/day9/example.txt")
	longestPath := findLongestPath(murder)
	fmt.Println("The longest path is ", longestPath)


	// 783 too low Max is 891
	murder2 := readInput("src/year_2015/day9/input.txt")
	longestPath2 := findLongestPath(murder2)
	fmt.Println("The longest path is ", longestPath2)
}
func Solve() {
	part1()
	part2()
}