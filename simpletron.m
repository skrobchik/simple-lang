function simpletron (codigo)
%codigo es un arreglo de 100 = instrucciones y memoria de maquina
%acumulador es variable de sistema
%nDLinea es contador de lineas
acumulador=0;
nDLinea=1;
while nDLinea<100
    
    incr=1;
    
    codA=num2str(codigo(nDLinea));
    %Se divide la instruccion de el espacio de memoria a usar
    instrux=str2num(codA(1:2));
    nEspDM=str2num(codA(3:4));
    
    switch instrux
        case 10
            disp(['entrada de teclado y guarda en  memoria ' num2str(nEspDM)]);
            codigo(nEspDM)=input('\nSimpletron necesita valor\n');
            nDLinea=nDLinea+incr;
        case 11
            disp(['imprime contenido memoria ' num2str(nEspDM)]);
            disp(codigo(nEspDM));
            nDLinea=nDLinea+incr;
        case 20
            disp(['carga a acumulador contenido memoria ' num2str(nEspDM)]);
            acumulador=codigo(nEspDM);
            nDLinea=nDLinea+incr;
        case 21
            disp(['almacena acumulador en memoria ' num2str(nEspDM)]);
            codigo(nEspDM)=acumulador;
            nDLinea=nDLinea+incr;
        case 30
            disp(['suma contenido memoria ' num2str(nEspDM) ' a acumulador']);
            acumulador=acumulador+codigo(nEspDM)
            nDLinea=nDLinea+incr;
        case 31
            disp(['resta contenido memoria ' num2str(nEspDM) ' a acumulador']);
            acumulador=acumulador-codigo(nEspDM)
            nDLinea=nDLinea+incr;
        case 32
            disp(['divide contenido memoria ' num2str(nEspDM) ' entre acumulador']);
            acumulador=codigo(nEspDM)/acumulador;  %acumulador/codigo(nEspDM);
            nDLinea=nDLinea+incr;
        case 33
            disp(['multiplica contenido memoria ' num2str(nEspDM) ' a acumulador']);
            acumulador=acumulador*codigo(nEspDM);
            nDLinea=nDLinea+incr;
        case 40
            disp(['bifurca a ' num2str(nEspDM)]);
            nDLinea=nEspDM;
        case 41
            disp(['bifurca a ' num2str(nEspDM) ' si negativo']);
            if acumulador<0
                nDLinea=nEspDM;
            else
                nDLinea=nDLinea+incr;
            end
        case 42
            disp(['bifurca a ' num2str(nEspDM) ' si cero']);
            if acumulador==0
                nDLinea=nEspDM;
            else
                nDLinea=nDLinea+incr;
            end
        case 43
            disp('fin de programa');
            break
        otherwise
            disp('ERROR: Instruccion no encontrada');
            break
    end
end