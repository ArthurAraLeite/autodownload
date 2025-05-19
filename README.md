READ ME

### 🛠️ Steam Workshop Collection to SteamCMD `.bat` Generator

Este script em Python automatiza o processo de extração dos **IDs de mods** de uma coleção do Steam Workshop e gera um arquivo `.bat` com comandos prontos para serem usados no **SteamCMD**, facilitando o download em massa de conteúdos do Workshop.

---

### ✨ Funcionalidades

* ✅ Acessa a página da coleção via `requests`
* ✅ Extrai automaticamente todos os `mod IDs` com `BeautifulSoup`
* ✅ Remove duplicatas e organiza os IDs
* ✅ Gera um arquivo `baixar_mods.bat` contendo comandos do tipo:

  ```
  workshop_download_item <game_id> <mod_id>
  ```
* ✅ Pronto para ser usado diretamente com SteamCMD

---

### 💻 Como usar

1. **Instale as dependências**:

   ```
   pip install requests beautifulsoup4
   ```

2. **Edite o `colecao_id`** com o ID da sua coleção Steam.

3. **Execute o script**:

   ```
   python steam_collection_downloader.py
   ```

4. O script irá gerar um arquivo `baixar_mods.bat`.

5. **Abra o SteamCMD** e rode:

   ```
   steamcmd +login anonymous +runscript baixar_mods.bat
   ```

---

### 🧩 Requisitos

* Python 3.6+
* SteamCMD instalado e configurado
* A coleção precisa ser **pública**

---

### 📎 Exemplo de uso

```python
colecao_id = '3482851310'  # Substitua pelo ID da sua coleção
```
