package helpers

import (
	"encoding/json"
	"errors"
	"log"
	"net/http"
)

func ErrorResponse(w http.ResponseWriter, err error) {
	http.Error(w, err.Error(), http.StatusInternalServerError)
	log.Println(err)
}

func WriteJSONResponse(w http.ResponseWriter, data interface{}) error {
	jsonData, err := json.Marshal(data)
	if err != nil {
		return err
	}
	w.Header().Set("Content-Type", "application/json")
	_, err = w.Write(jsonData)
	return err
}

func CheckRequestBody(r *http.Request) error {
	if r.Body == nil {
		return errors.New("request body is empty")
	}
	err := json.NewDecoder(r.Body).Decode(&map[string]interface{}{})
	if err != nil {
		return err
	}
	return nil
}