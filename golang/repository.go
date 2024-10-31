// this example is equvalent of python function overriding, dependency injection & repository pattern combined
package main

import "fmt"

type Writer interface {
	write()
}
type Speaker interface {
	speak()
}

type Repo interface {
	Speaker
}

type OriginalWriter struct{}
type OriginalSpeaker struct {
	w Writer
}
type Original struct {
	Speaker
}

func (o OriginalWriter) write() {
	fmt.Println("Writing from Original")
}
func (o OriginalSpeaker) speak() {
	o.w.write()
	fmt.Println("Speaking from Original")
}

type NewWriter struct{}

func (n NewWriter) write() {
	fmt.Println("Writing from New")
}

type NewRepo interface {
	Writer
	Repo
}
type New struct {
	Writer
	Speaker
}

func GetNewRepo() NewRepo {
	return &New{
		Writer: NewWriter{},
		Speaker: OriginalSpeaker{
			w: NewWriter{},
		},
	}
}

func GetOriginalRepo() Repo {
	return &Original{
		Speaker: OriginalSpeaker{
			w: OriginalWriter{},
		},
	}
}

func main() {
	// o := Original{
	// 	s: OriginalSpeaker{
	// 		w: NewWriter{},
	// 	},
	// }
	// o.s.speak()
	r := GetOriginalRepo()
	// r.speak()
	r.speak()

	r = GetNewRepo()
	// r.write()
	r.speak()

	newRepo := GetNewRepo()
	newRepo.write()
	newRepo.speak()

	fmt.Println("\n")

}
