package main

import (
	"log"
	"net/http"
)

func main() {
	http.Handle("/learn/", http.StripPrefix("/learn/", http.FileServer(http.Dir("."))))
	log.Fatal(http.ListenAndServe(":8080", nil))
}
