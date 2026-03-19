# TestoMaestro

Gestione avanzata di file testuali a larghezza fissa con strumenti di ordinamento, filtraggio e anteprima.  
TestoMaestro è pensato per chi ha bisogno di manipolare file di testo complessi in modo semplice, intuitivo e affidabile, con una GUI chiara e moderna.

## Obiettivi del progetto

- Fornire uno strumento **facile da usare** per manipolare file testuali
- Supportare **file a larghezza fissa**
- Permettere **ordinamento multi-criterio** su colonne o intervalli di colonne
- Applicare **filtri multipli** su valori presenti nelle colonne
- Mostrare **anteprima** delle trasformazioni con evidenziazione dei filtri e ordinamenti
- Salvare automaticamente i file modificati con nome generato in base al timestamp
- Fornire un **tool stabile e condivisibile**, pronto per GitHub o distribuzione interna

## Funzionalità principali

### 1. Caricamento file
- Selezione file da percorso locale o **tramite drag & drop** direttamente nell’area dell'applicazione
- Supporto per file a larghezza fissa
- Preview delle prime **n righe** nel widget dedicato
- GUI reattiva con scroll verticale e orizzontale in base al contenuto del box di anteprima

### 2. Ordinamento
- Ordinamento su intervalli di colonne multipli
- Direzione **ascendente o discendente** per ciascun intervallo/colonna
- Multi-criterio: esempio, prima colonne 1–3 ascendente, poi colonne 5-8 discendente

### 3. Filtri
- Applicazione di filtri multipli su intervalli di colonne
- Evidenzia le colonne filtrate direttamente nell’anteprima.
- Supporta operatori di confronto: `=`, `!=`, `>`, `<`, `>=`, `<=`, `~`, `!~`

### 4. Anteprima
- Visualizzazione delle prime **n righe** prima e dopo le trasformazioni
- Evidenza delle colonne selezionate (Da e A) per agevolare l'impostazione dei filtri e degli ordinamenti
- Evidenziazione delle colonne interessate dai filtri e dagli ordinamenti

### 5. Output
- File salvato automaticamente con nome generato secondo pattern:  
  `<nomefile>_TestoMaestro_<timestamp>.<estensione originale>`
- Filtri e ordinamenti applicati in memoria prima della scrittura

## Architettura del progetto

TestoMaestro/
├── src/           # codice sorgente
│   ├── [main.py](src/main.py)    # punto di ingresso
│   ├── [testomaestro_gui.py](src/testomaestro_gui.py)  # gestione GUI principale
│   ├── [engine.py](src/engine.py)  # motore di elaborazione (filtri, ordinamenti)
│   ├── [utils.py](src/utils.py)   # funzioni di supporto
│   └── [info_app.py](src/info_app.py) # popup info e copyright
├── examples/      # esempi di file testuali
├── dist/          # eseguibile compilato
├── README.md      # documentazione
└── LICENSE.md     # licenza MIT

## Considerazioni tecniche

- Python gestisce i file **in memoria**, ottimo per file piccoli e medi (<500 MB)
- GUI leggera, realizzata con **Tkinter**, con layout reattivo per schermi di diverse dimensioni
- Drag & drop dei file supportato tramite **tkinterdnd2**
- Per chi desidera ricompilare l’app da sorgente, sono richieste le librerie: `pandas` (gestione CSV), `tkinterdnd2` (drag & drop)
- L’EXE distribuito è **standalone**, non richiede Python né installazione di librerie aggiuntive
- Il motore interno (`engine.py`) applica filtri e ordinamenti in modo sequenziale, mantenendo consistenza tra anteprima e output

## Note future / TODO

- Mostrare info dimensione file caricato e lunghezza righe
- Gestione alert se file caricato > <parametro soglia MB>
- Possibilità di scegliere le righe da estrarre: prime "n" righe o righe dalla "n" alla "n" o multiple scelte (scegliere se applicare queste condizioni sul di input o sul file di output; considerare se questa estrazione è compatibile con i filtri e gli ordinamenti applicati dall'utente)
- Scelta di poter caricare in anteprima più di 10 (default)
- Salvataggio in memoria cartella da dove prendere i file (directory preferita)
- Utilizzo "cython" cone compilatore "python vs c" per migliorare prestazioni
- Gestione "replace" - sostituzione dati
- Gestione duplicati (flag o eliminazione)
- Gestione ordinamenti e filtri per tipologia file CSV
- Possibilità di salvare **preset di filtri e ordinamenti**
- Pipeline batch per elaborare **più file in sequenza**
- Ottimizzazione per file molto grandi (>500 MB) con approccio **chunk + merge**
- Info/chiarimento visivo per modalità ordinamento (priorità a Maiuscole, Minuscole, caratteri speciali...)
- Possibilità di aprire su app il file prodotto (se troppo grande aprire solo una parte) o apertura cartella con file prodotto già selezionato

---

**TestoMaestro** è pensato per la gestione pratica e professionale di file testuali, con un’interfaccia **chiara**, **moderna** e **responsiva**, pronta per uso personale o distribuzione.  

**Licenza:** MIT (vedi `LICENSE`)  
**Copyright:** (c) 2026 Igor Vesentini