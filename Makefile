
UIKIT:=Flat-UI-master

output:
	mkdir output
	cd $(UIKIT); tar cf - css fonts images js sass | (cd ../output ; tar xvf - )
	cd www; tar cf - . | (cd ../output; tar xvf - )

publish:
	s3cmd sync www/ s3://whybitcoinisbetterthanx.com

clean:
	rm -rf output

