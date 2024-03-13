#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include<assert.h>
#define MAX_CHARACTERS 1005
#define MAX_PARAGRAPHS 5
#define MAX_SENTENCES 30
#define MAX_WORDS 100


char* create_word() {

    char* word = (char*)malloc(MAX_CHARACTERS * sizeof(char));

    return word;
}


char** create_sentence() {

    char** sentence = (char**)malloc(MAX_WORDS * sizeof(char*));

    for (size_t word=0; word < MAX_WORDS; ++word) {
        sentence[word] = create_word();
    }

    return sentence;
}


char*** create_paragraph() {

    char*** paragraph = (char***)malloc(MAX_SENTENCES * sizeof(char**));

    for (size_t sentence=0; sentence < MAX_SENTENCES; ++sentence) {
        paragraph[sentence] = create_sentence();
    }

    return paragraph;
}


char**** create_document() {

    char**** document = (char****)malloc(MAX_PARAGRAPHS * sizeof(char***));

    for (size_t paragraph=0; paragraph < MAX_PARAGRAPHS; ++paragraph) {
        document[paragraph] = create_paragraph();
    }

    return document;
}


char* kth_word_in_mth_sentence_of_nth_paragraph(const char**** document,
                                                const int word,
                                                const int sentence,
                                                const int paragraph)
{

    return document[paragraph-1][sentence-1][word-1];
}

char** kth_sentence_in_mth_paragraph(const char**** document,
                                     const int sentence,
                                     const int paragraph)
{

    return document[paragraph-1][sentence-1];
}

char*** kth_paragraph(const char**** document, const int paragraph) {

    return document[paragraph-1];
}


char**** get_document(const char* text) {
    char**** document = create_document();

    char* current_word = NULL;
    const char* separators = " .,!?";

    size_t d_paragraph = 0;
    size_t p_sentence  = 0;
    size_t s_word      = 0;

    size_t w_start = 0;
    size_t w_end   = 0;

    for (size_t ch=0; text[ch]; ++ch) {

        if (strchr(separators, text[ch])) {
            current_word = document[d_paragraph][p_sentence][s_word];

            strncpy(current_word, &text[w_start], w_end-w_start);

            w_start = w_end+1;
            ++s_word;
        }

        if (text[ch] == '.') {
            s_word = 0;
            ++p_sentence;
        }

        if (text[ch] == '\n') {
            p_sentence = 0;
            ++d_paragraph;
            ++w_start;
        }

        ++w_end;
    }

    return document;
}


char* get_input_text() {
    int paragraph_count;
    scanf("%d", &paragraph_count);

    char p[MAX_PARAGRAPHS][MAX_CHARACTERS], doc[MAX_CHARACTERS];
    memset(doc, 0, sizeof(doc));
    getchar();
    for (int i = 0; i < paragraph_count; i++) {
        scanf("%[^\n]%*c", p[i]);
        strcat(doc, p[i]);
        if (i != paragraph_count - 1)
            strcat(doc, "\n");
    }

    char* returnDoc = (char*)malloc((strlen (doc)+1) * (sizeof(char)));
    strcpy(returnDoc, doc);
    return returnDoc;
}

void print_word(char* word) {
    printf("%s", word);
}

void print_sentence(char** sentence) {
    int word_count;
    scanf("%d", &word_count);
    for(int i = 0; i < word_count; i++){
        printf("%s", sentence[i]);
        if( i != word_count - 1)
            printf(" ");
    }
}

void print_paragraph(char*** paragraph) {
    int sentence_count;
    scanf("%d", &sentence_count);
    for (int i = 0; i < sentence_count; i++) {
        print_sentence(*(paragraph + i));
        printf(".");
    }
}

int main()
{
    char* text = get_input_text();
    char**** document = get_document(text);

    int q;
    scanf("%d", &q);

    while (q--) {
        int type;
        scanf("%d", &type);

        if (type == 3){
            int k, m, n;
            scanf("%d %d %d", &k, &m, &n);
            char* word = kth_word_in_mth_sentence_of_nth_paragraph(document, k, m, n);
            print_word(word);
        }

        else if (type == 2){
            int k, m;
            scanf("%d %d", &k, &m);
            char** sentence = kth_sentence_in_mth_paragraph(document, k, m);
            print_sentence(sentence);
        }

        else{
            int k;
            scanf("%d", &k);
            char*** paragraph = kth_paragraph(document, k);
            print_paragraph(paragraph);
        }
        printf("\n");
    }
}