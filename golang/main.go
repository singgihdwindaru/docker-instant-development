package main

import (
	"fmt"
	"log"
	"net/http"

	"github.com/gorilla/mux"
)

func main() {
	// Initialize the router
	router := mux.NewRouter()

	// Route for the root endpoint
	router.HandleFunc("/", func(w http.ResponseWriter, r *http.Request) {
		fmt.Fprintf(w, "Hello changes!")
	})

	// Start the HTTP server
	log.Fatal(http.ListenAndServe(":8080", router))
}
