
# Real-Time Person Detection via RTSP Stream

Questo progetto utilizza un modello YOLOv10 per rilevare persone in tempo reale da un flusso video RTSP.

## Requisiti

Assicurati di avere i seguenti pacchetti installati:

- `opencv-python`
- `ultralytics`
- `supervision`

Puoi installarli usando `pip`:

```bash
pip install opencv-python ultralytics supervision
```


## Configurazione
1. Modello YOLOv10: Assicurati di avere il file dei pesi best.pt del modello YOLOv10. Puoi addestrare il modello sui tuoi dati o scaricare un modello pre-addestrato.
2. URL RTSP: Inserisci l'URL RTSP della tua telecamera nel codice.

## URL RTSP

Nel file Python, sostituisci la stringa rtsp_url con l'URL della tua telecamera RTSP:

```python
rtsp_url = "rtsp://utente:password@indirizzo_ip:porta"
```
## Aspetti tecnici
### Cos'è il protocollo RTSP?
RTSP (Real-Time Streaming Protocol) è un protocollo di rete progettato per il controllo di server di streaming multimediale. Il protocollo consente il controllo a distanza di flussi multimediali in tempo reale. Ad esempio, viene comunemente utilizzato per visualizzare il video in diretta delle telecamere IP. Il protocollo RTSP gestisce la trasmissione del flusso video e permette funzioni come la riproduzione, la pausa e la registrazione.
### Cos'è YOLO?
YOLO (You Only Look Once) è una famiglia di algoritmi di visione artificiale utilizzati per il rilevamento in tempo reale di oggetti in immagini e video. YOLO è noto per la sua velocità e accuratezza. L'algoritmo divide l'immagine in una griglia e passa attraverso ogni cella della griglia per prevedere bounding box e probabilità per ciascun oggetto. YOLOv10 è una versione avanzata del modello, che offre miglioramenti in termini di velocità e precisione.
### Come funziona il threading video?
Il threading è una tecnica di programmazione che consente l'esecuzione simultanea di più operazioni. In questo progetto, utilizziamo un thread separato per catturare i frame dal flusso RTSP in tempo reale. La classe VideoCaptureThreading gestisce la lettura dei frame in un thread separato per ridurre la latenza e migliorare la performance del rilevamento in tempo reale. Il metodo update del thread legge continuamente i frame dalla telecamera e li memorizza in variabili condivise, che possono essere lette dal thread principale per il rilevamento degli oggetti.

