package main

import(
	"log"
	"net/http"
	"fmt"
)

func main() {
	// Serve static content from the current directory on port 8080 
	go func() {log.Fatal(http.ListenAndServe(":8080", http.FileServer(http.Dir("."))))}()

	fmt.Println("\nServer started on port 8080")
	fmt.Println("\nPress Enter to continue")
	fmt.Scanln() // Wait for Enter key
}

