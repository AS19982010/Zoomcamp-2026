# Data Engineering Zoomcamp 2026 - Module 5 Homework
## Temat: Data Platforms - Automatyzacja rurociągu danych z Bruin

### 📝 Opis projektu
Niniejsze repozytorium zawiera rozwiązanie pracy domowej z modułu poświęconego platformom danych. Zadanie polegało na wykorzystaniu narzędzia **Bruin** do stworzenia i zautomatyzowania rurociągu danych (ELT) opartego na danych o przejazdach taksówek w Nowym Jorku (NYC Yellow Taxi).

**Główne etapy pracy:**
1.  **Inicjalizacja środowiska:** Skonfigurowanie Bruin lokalnie na systemie macOS.
2.  **Modelowanie danych:** Przygotowanie skryptów SQL (`staging` oraz `reporting`) transformujących surowe dane.
3.  **Zarządzanie zależnościami:** Zdefiniowanie grafu pochodzenia danych (Data Lineage) pomiędzy zadaniami.
4.  **Walidacja:** Sprawdzenie poprawności definicji rurociągu i zgodności ze strategiami materializacji.

---

### 📊 Odpowiedzi na pytania (Homework 2026)

#### **Question 1: Bruin Pipeline Structure**
* **Pytanie:** In a Bruin project, what are the required files/directories?
* **Odpowiedź:** **`.bruin.yml` and `pipeline/` with `pipeline.yml` and `assets/`**
* **Uzasadnienie:** Bruin wymaga głównego pliku konfiguracyjnego projektu oraz folderu rurociągu zawierającego jego definicję i zasoby.

#### **Question 2: Materialization Strategies**
* **Pytanie:** Which incremental strategy is best for processing a specific interval period by deleting and inserting data for that time period?
* **Odpowiedź:** **`time_interval` - incremental based on a time column**
* **Uzasadnienie:** Ta strategia pozwala na precyzyjne zastępowanie danych w określonym oknie czasowym (np. miesiąc), co jest kluczowe przy danych takich jak NYC Taxi.

#### **Question 3: Pipeline Variables**
* **Pytanie:** How do you override a variable (e.g., `taxi_types`) when running the pipeline?
* **Odpowiedź:** **`bruin run --var 'taxi_types=["yellow"]'`**
* **Uzasadnienie:** Flaga `--var` służy do nadpisywania zmiennych zdefiniowanych w `pipeline.yml`.

#### **Question 4: Running with Dependencies**
* **Pytanie:** Which command should you use to run an asset plus all downstream assets?
* **Odpowiedź:** **`bruin run --select ingestion.trips+`**
* **Uzasadnienie:** Symbol `+` na końcu nazwy assetu w Bruin oznacza "ten zasób oraz wszystko, co od niego zależy" (downstream).



#### **Question 5: Quality Checks**
* **Pytanie:** Which quality check ensures the `pickup_datetime` column never has NULL values?
* **Odpowiedź:** **`name: not_null`**
* **Uzasadnienie:** Jest to wbudowany test jakości w Bruin, który automatycznie sprawdza brak pustych wartości w kolumnie.

#### **Question 6: Lineage and Dependencies**
* **Pytanie:** Which Bruin command should you use to visualize the dependency graph?
* **Odpowiedź:** **`bruin lineage`**
* **Uzasadnienie:** Komenda ta generuje wizualizację powiązań między wszystkimi assetami w projekcie.

#### **Question 7: First-Time Run**
* **Pytanie:** What flag should you use to ensure tables are created from scratch (e.g., on a new DuckDB)?
* **Odpowiedź:** **`--full-refresh`**
* **Uzasadnienie:** Ta flaga ignoruje tryb przyrostowy (incremental) i wymusza przebudowanie wszystkich tabel od podstaw.

--- 

### 🛠️ Wykorzystane narzędzia
* **Bruin CLI**: Do orkiestracji i walidacji rurociągu.
* **DuckDB**: Wykorzystana jako lokalna baza danych do testów.
* **Google BigQuery**: Docelowy magazyn danych (Data Warehouse).
* **VS Code**: Środowisko programistyczne z rozszerzeniem Bruin.

