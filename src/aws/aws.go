package aws

import (
	"strings"

	"github.com/darthguinea/golib/log"
	"gopkg.in/go-ini/ini.v1"
)

func loadFiles(credsPath, configPath *string) (*ini.File, *ini.File) {
	creds, errCreds := ini.Load(*credsPath)
	if errCreds != nil {
		log.Fatal(errCreds)
	}
	cfg, errCfg := ini.Load(*configPath)
	if errCfg != nil {
		log.Fatal(errCfg)
	}
	return creds, cfg
}

func List(credsPath, configPath *string) {
	creds, _ := loadFiles(credsPath, configPath)
	log.Print("You have the following AWS accounts:")
	current := ""
	for _, c := range creds.Sections() {
		if strings.Compare("default", c.Name()) == 0 {
			current = c.Key("aws_access_key_id").String()
			log.Print("%20v%30v", c.Name(), c.Key("aws_access_key_id").String())
		} else {
			if strings.Compare("DEFAULT", c.Name()) != 0 {
				if strings.Compare(current, c.Key("aws_access_key_id").String()) == 0 {
					log.Print("%20v*%29v", c.Name(), c.Key("aws_access_key_id").String())
				} else {
					log.Print("%20v%30v", c.Name(), c.Key("aws_access_key_id").String())
				}
			}
		}
	}
}

func Set(credsPath, configPath, awsAccount *string) {
	creds, config := loadFiles(credsPath, configPath)

	// Set credentials
	for _, c := range creds.Sections() {
		if strings.Compare(*awsAccount, c.Name()) == 0 {
			log.Print("Using AWS config %v", c.Name())

			// Get the keys
			access_key_id, _ := c.GetKey("aws_access_key_id")
			secret_access_key, _ := c.GetKey("aws_secret_access_key")

			// Set the keys
			creds.Section("default").Key("aws_access_key_id").SetValue(access_key_id.Value())
			creds.Section("default").Key("aws_secret_access_key").SetValue(secret_access_key.Value())
			creds.SaveTo(*credsPath)
		}
	}

	// Set config
	for _, c := range config.Sections() {
		if strings.Compare(*awsAccount, c.Name()) == 0 {

			// Get the keys
			region, _ := c.GetKey("region")
			output, _ := c.GetKey("output")

			// Set the keys
			config.Section("default").Key("region").SetValue(region.Value())
			config.Section("default").Key("output").SetValue(output.Value())
			config.SaveTo(*configPath)
		}
	}
}
