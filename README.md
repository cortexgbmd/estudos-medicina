# 📚 Materiais de Estudo · Medicina

Portal único que reúne os materiais de estudo de Medicina (bancos de questões, resumões, dossiês, flashcards e sites de estudo), organizados por **matéria → período → tipo**, com **busca**, **filtro por matéria** e seção de **recentes**.

🔗 **No ar:** https://cortexgbmd.github.io/estudos-medicina/

> Feito por Gabriel Medeiros — para compartilhar com a turma. Cada material é um HTML autossuficiente; a home (`index.html`) é só o índice.

---

## 🗂️ Estrutura

```
estudos-medicina/
├── index.html              ← a HOME (GERADA — não edite à mão; veja "Como a home é montada")
├── data/
│   └── materials.json      ← FONTE DA VERDADE: a lista de todos os materiais
├── tools/
│   ├── template.html       ← o molde da home (com o placeholder __MATERIALS_JSON__)
│   └── build.py            ← injeta o materials.json no template e gera o index.html
├── assets/                 ← logo + favicons (logo.png, favicon-32.png, apple-touch-icon.png…)
├── .nojekyll               ← desliga o Jekyll do GitHub Pages (serve as pastas como estão)
│
├── farmacologia/           ← uma pasta por MATÉRIA
│   ├── p2/                  ← subpasta por PERÍODO (quando aplicável)
│   │   ├── site/           ← subpasta por TIPO (site, questoes, resumao, dossie…)
│   │   │   ├── index.html  ← o material em si
│   │   │   └── img/        ← imagens do material (caminhos RELATIVOS)
│   │   ├── questoes/
│   │   └── resumao/
│   └── p3/ …
├── microbiologia/ …
├── anatomia-patologica/ …
└── … (11 matérias no total)
```

### Convenções
- **Caminhos relativos sempre.** Cada material referencia seus assets como `img/...` (nunca `/img/...`), pra funcionar dentro da subpasta.
- **Slugs sem acento/espaço** nas pastas: `anatomia-patologica`, `endocrinologia`, etc.
- **Tipos comuns:** `site` (site de estudo), `questoes` (banco de questões), `resumao` (resumão pré-prova), `dossie`, `flashcards`, `cram`, `decorar`.
- A home abre em **modo escuro** por padrão, com botão ☀️/🌙 que lembra a escolha (localStorage).

---

## 🎓 Matéria → Semestre (FASM, currículo 2023)

O semestre de cada material é **derivado da matéria** por esta tabela (currículo modular da Faculdade Santa Marcelina). Por isso, ao adicionar um HTML, **não é preciso informar o semestre** — ele sai da matéria.

| Matéria | Semestre | Onde fica no currículo |
|---|---|---|
| Imunologia | **3º** | Módulo Agressão e Defesa I |
| Microbiologia | **3º** | Módulo Agressão e Defesa I |
| DIP — Infecto & Parasito | **3º** | Módulo Agressão e Defesa I |
| Farmacologia | **3º** | Módulo Agressão e Defesa I/II |
| Anatomia Patológica | **3º** | Módulo Agressão e Defesa I/II |
| Cardiologia / Semiologia | **3º** | Propedêutica e Semiologia III |
| Bioestatística | **3º** | Epidemiologia e Bioestatística II |
| Endocrinologia | **2º** | Bases da Fisiologia Humana (endócrino) |
| APH — Pré-Hospitalar | **2º** | Atendimento Pré-Hospitalar do Trauma |
| Geriatria | **4º** | Saúde do Idoso (Atenção Primária IV) |
| Dermatologia | **4º** | Saúde da Criança (dermato neonatal) |

> ⚠️ O currículo é **modular/integrado** (os assuntos vivem dentro de módulos, não como disciplinas isoladas), então o semestre de alguns temas transversais (Cardio, Geriatria, Endócrino, Dermato) é uma **aproximação** — ajuste livremente em `data/materials.json` ou avise no `/lancar`.

No site, isso vira: um **badge "Xº sem"** em cada card, uma linha de **chips por semestre** (filtro) e o semestre entra na **busca**.

---

## 🔧 Como a home é montada

A home **não é editada à mão**. Ela é gerada a partir de `data/materials.json`:

```bash
python3 tools/build.py
```

Isso pega `tools/template.html`, substitui o placeholder `__MATERIALS_JSON__` pelo conteúdo de `data/materials.json` e escreve o `index.html`. Toda a busca/filtro/recentes roda no navegador (vanilla JS, sem dependências externas).

### Formato de cada material em `data/materials.json`
```json
{
  "materia": "Farmacologia",            // rótulo exibido
  "materia_key": "farmacologia",        // slug da pasta (= 1ª pasta da url)
  "periodo": "P2",                      // "P1".."P4" ou "" se não houver
  "semestre": 3,                        // semestre do currículo (derivado da matéria — ver tabela)
  "tipo": "Banco de questões",          // rótulo do tipo
  "title": "Banco de Questões — Farmacologia P2",
  "url": "farmacologia/p2/questoes/",   // caminho RELATIVO até o material
  "date": "2026-04-05",                 // AAAA-MM-DD (alimenta os "Recentes")
  "repo": "farmacop2questoes"           // opcional: repo de origem (histórico)
}
```

---

## ➕ Como adicionar um novo material

**Jeito fácil (recomendado):** use a skill **`/lancar-estudo`** no Claude Code — anexe o(s) HTML(s), que ela coloca na pasta certa, atualiza o `materials.json`, regenera e dá push.

**Na mão (3 passos):**
1. Crie a pasta `materia/periodo/tipo/` e coloque o material como `index.html` (e sua pasta `img/` se tiver).
2. Acrescente um objeto no array de `data/materials.json` (use o formato acima; `date` = hoje).
3. Rode `python3 tools/build.py`, confira o `index.html`, e faça commit + push.

O GitHub Pages publica sozinho a cada push na branch `main`.

---

## 🌐 Deploy
GitHub Pages servindo a branch `main` na raiz (`/`). O `.nojekyll` garante que nada seja reprocessado. Qualquer push atualiza o site em ~1 min.
