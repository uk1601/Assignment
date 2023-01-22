#!/bin/bash
awk '{for (i=1;i<=NF;i++) if($(i)!=$(i+1)) printf("%s%s",$i,FS)}{printf("\n")}'