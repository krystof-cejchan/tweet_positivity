import java.io.*;

public class RemoveTextFromFile {
    public static void main(String[] args) {
        try {
            // Open the file
            File file = new File("C:\\Users\\vecer\\PycharmProjects\\tweet_positivity\\newCSV.txt");
            BufferedReader reader = new BufferedReader(new FileReader(file));

            // Create a StringBuilder to store the modified text
            StringBuilder stringBuilder = new StringBuilder();

            boolean insideTimezone = false;
            boolean insideSentiment = false;

            int c;
            while ((c = reader.read()) != -1) {
                char character = (char) c;

                // Check if the character is "+00:00,"
                if (character == '+' && reader.ready()) {
                    char nextChar = (char) reader.read();
                    if (nextChar == '0' && reader.ready()) {
                        char nextNextChar = (char) reader.read();
                        if (nextNextChar == '0' && reader.ready()) {
                            char nextNextNextChar = (char) reader.read();
                            if (nextNextNextChar == ':' && reader.ready()) {
                                char nextNextNextNextChar = (char) reader.read();
                                if (nextNextNextNextChar == '0' && reader.ready()) {
                                    char nextNextNextNextNextChar = (char) reader.read();
                                    if (nextNextNextNextNextChar == '0' && reader.ready()) {
                                        char nextNextNextNextNextNextChar = (char) reader.read();
                                        if (nextNextNextNextNextNextChar == ',') {
                                            insideTimezone = true;
                                        }
                                    }
                                }
                            }
                        }
                    }
                }

                // Check if the character is "P", "N", or "E"
                if (character == 'P' || character == 'N' || character == 'E') {
                    String phrase = "";
                    phrase += character;

                    if (reader.ready()) {
                        char nextChar = (char) reader.read();
                        phrase += nextChar;

                        if (reader.ready()) {
                            char nextNextChar = (char) reader.read();
                            phrase += nextNextChar;
                            if (reader.ready()) {
                            char nextNextChar1 = (char) reader.read();
                            phrase += nextNextChar1;
                            if (reader.ready()) {
                            char nextNextChar2 = (char) reader.read();
                            phrase += nextNextChar2;
                            if (reader.ready()) {
                            char nextNextChar3 = (char) reader.read();
                            phrase += nextNextChar3;

                            if (phrase.equals("POSITI") || phrase.equals("NEGATI") || phrase.equals("NEUTRA")) {
                                insideSentiment = true;
                            }
                        }}}}
                    }
                }

                // Remove characters between (not including) "+00:00," and the text with values of "POSITIVE", "NEGATIVE", or "NEUTRAL"
                if (insideTimezone || insideSentiment) {
                    stringBuilder.append(character);
                }

                // Check if we've reached the end of the phrase
                if (insideSentiment && character == ' ') {
                    insideSentiment = false;
                }

                // Check if we've reached the end of the timezone text
                if (insideTimezone && character == ' ') {
                    insideTimezone = false;
                }
            }
            reader.close();

            // Write the modified text back to the file
            FileWriter writer = new FileWriter(file);
            writer.write(stringBuilder.toString());
            writer.close();
        } catch (IOException e) {
            e.printStackTrace();
        }
    }
}
