int pines[]={52,50,48,46,42,40,38,36};
int valores[8]={0,0,0,0,0,0,0,0};
int val; // variable para almacenar el valor leído del potenciómetro

void setup() {
  // inicializamos la comunicación serial para poder ver los valores leídos del potenciómetro en la consola
  Serial.begin(9600);
  for(int i=0; i<8; i++){
    pinMode(i,INPUT);
  }
}

void loop() {
  //val = digitalRead(2); // leemos el valor del potenciómetro en el pin analógico
  for(int i=0;i<8;i++){
    val = digitalRead(pines[i]);
    valores[i]=val;
  }                                                                       
  for(int i=0;i<8;i++){
    //Serial.print("Entrada ");
    //Serial.print(i);
    //Serial.print(" :");
    Serial.print(valores[i]);
    //Serial.print("\t");
  }

  Serial.println();
  for(int i=0;i<8;i++){
    valores[i]=0;
  }
  //Serial.println(val); // imprimimos el valor leído del potenciómetro en la consola
  delay(1000); // esperamos 100 milisegundos para volver a leer el valor del potenciómetro
}
