FILE* inputFile = fopen(inputFileName, "r");
if (inputFile == NULL) {
    printf("Error opening input file.\n");
    return 1;
}

FILE* outputFile = fopen(outputFileName, "w");
if (outputFile == NULL) {
    printf("Error opening output file.\n");
    return 1;
}

while (fgets(line, MAX_LINE_LENGTH, inputFile) != NULL) {
    if (strlen(line) < 19)
        continue;
    char modifiedLine[MAX_LINE_LENGTH];
    sprintf(modifiedLine, "\"%.*s\"%s", 19, line, line + 19);
    fputs(modifiedLine, outputFile);
    fputc('\n', outputFile);
}

fclose(inputFile);
fclose(outputFile);

printf("File modified successfully.\n");
return 0;











































































































































































