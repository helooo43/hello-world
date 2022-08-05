package main

import (
    "fmt"
    "log"
	"os"
	"os/exec"
	"bufio"
)

func logFatal(err error){
    if err != nil {
        log.Fatal(err)
        return
    }
}


func contain(x rune, y string) bool{
    for _, v := range y{
        if v == x{
            return true}
        }
	return false
}

func main(){
var com string
var arg string

	for{
		fmt.Printf("$:")
		scanner := bufio.NewScanner(os.Stdin)
		scanner.Scan()
		cmd := scanner.Text()
		
		
		if cmd[:3] == "cd "{
			os.Chdir(cmd[3:])
			out, err := os.Getwd()
			logFatal(err)
			fmt.Println(out)

		}else if contain(' ', cmd){
			for i, v := range cmd{
				
				if string(v) == " "{
					com = cmd[:i]
					arg = cmd[i + 1:]
					fmt.Println(i, string(v))}
			}

			out, err := exec.Command(com, arg).Output()
			logFatal(err)
			fmt.Println(string(out))
		
		}else{
			out, err := exec.Command(cmd).Output()
			logFatal(err)
			fmt.Println(string(out))
		}

	}

}
