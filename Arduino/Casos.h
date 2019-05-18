#if !defined(CASOS_H)
#define CASOS_H
#include <map>
#include <list>
#define espacio 0
#define punto 1
#define guion 2

class Casos {
private:
    list <int> codigos[27];
    map<char, codigos> caracteres;

public:
    void inicializar();
    void cadenaAmorseSonido(char* cadena){

    }
};

void Casos::inicializar(){
    //a
    codigos[0].push_back(punto);
    codigos[0].push_back(guion);
    //b
    codigos[1].push_back(guion);
    codigos[1].push_back(punto);
    codigos[1].push_back(punto);
    codigos[1].push_back(punto);
    //c 
    codigos[2].push_back(guion);
    codigos[2].push_back(punto);
    codigos[2].push_back(guion);
    codigos[2].push_back(punto);
    //d
    codigos[3].push_back(guion);
    codigos[3].push_back(punto);
    codigos[3].push_back(punto);
    //e
    codigos[4].push_back(punto);
    //f
    codigos[5].push_back(punto);
    codigos[5].push_back(punto);
    codigos[5].push_back(guion);
    codigos[5].push_back(punto);
    //g
    codigos[6].push_back(guion);
    codigos[6].push_back(guion);
    codigos[6].push_back(punto);
    //h
    codigos[7].push_back(punto);
    codigos[7].push_back(punto);
    codigos[7].push_back(punto);
    codigos[7].push_back(punto);
    //i
    codigos[8].push_back(punto);
    codigos[8].push_back(punto);
    //j
    codigos[9].push_back(punto);
    codigos[9].push_back(guion);
    codigos[9].push_back(guion);
    codigos[9].push_back(guion);
    //k
    codigos[10].push_back(guion);
    codigos[10].push_back(punto);
    codigos[10].push_back(guion);
    //l
    codigos[11].push_back(punto);
    codigos[11].push_back(guion);
    codigos[11].push_back(punto);
    codigos[11].push_back(punto);
    //m
    codigos[12].push_back(guion);
    codigos[12].push_back(guion);
    //n
    codigos[13].push_back(guion);
    codigos[13].push_back(punto);
    //o
    codigos[14].push_back(guion);
    codigos[14].push_back(guion);
    codigos[14].push_back(guion);
    //p
    codigos[15].push_back(punto);
    codigos[15].push_back(guion);
    codigos[15].push_back(guion);
    codigos[15].push_back(punto);
    
}

#endif // CASOS_H
