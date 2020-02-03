package main

import (
	"flag"
	"os"

	"./src/aws"

	"github.com/darthguinea/golib/iv"
	"github.com/darthguinea/golib/log"
)

func main() {
	var (
		flagVerbose bool
		flagDebug   bool
	)

	flag.BoolVar(&flagVerbose, "v", false, "-v verbose logging")
	flag.BoolVar(&flagDebug, "D", false, "-D very verbose logging")
	flag.Parse()

	path := "~/.aws"
	iv.ExpandPath(&path)
	conf := path + "/config"
	creds := path + "/credentials"

	if flagVerbose {
		log.SetLevel(log.INFO)
		log.Info("Log level INFO set.")
	}
	if flagDebug {
		log.SetLevel(log.DEBUG)
		log.Debug("God mode.")
	}

	if len(os.Args) == 2 {
		aws.Set(&creds, &conf, &os.Args[1])
	} else {
		aws.List(&creds, &conf)
	}
}
