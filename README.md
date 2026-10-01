# RELRaE Evaluation

This repository contains the results generated during the evaluation of the
[RELRaE](https://github.com/KE-UniLiv/RELRaE_2) framework and its modules.

## Repository Structure

Each of the main experiments and the code relating to it will be present in the
root of the repository. Any additional files relating to that experiment will be
noted as needed. Each part of the overall evaluation will be explained in this
`README.md` file, along with additional steps such as configuration settings required
to repeat the experiments.

## Getting Started

After cloning this repository, we recommend setting up a virtual environment (`venv`)
with a local python version of `3.12.4`. Then install the RELRaE framework with
the following command:

`pip install relrae==0.9.2`

**NOTE: MAKE SURE THE VERSION MATCHES THE ONE USED FOR THE EXPERIMENTS**

Then, to set up the correct repository structure, run the command:

`relrae init`

This should create the `/relrae_components/` directory, in which, the assets and
configurations RELRaE requires to function are stored and template files are generated.

## Preliminary Experiments

### P.a - Prompt Selection

A key part of RELRaE is the use of Large Language Models (LLMs) to evaluate and
refine the relationships captured by the naive rules-based module, RuBREx. As
the structure and linguistic features of the prompt can affect the responses given
by the model, it is important to select a prompt that can guide a model towards
a correct answer.

We acknowledge that different LLMs will perform differently to different prompts,
however, to limit the scope of this preliminary experiment we chose not to
tailor the prompt to each model. Additionally RELRaE supports few-shot prompting
for both LLM tasks which has been shown to reduce the input sensitivity of
LLMs \[1\].

For this test, we use Claude Sonnet 5 through the web interface. We elect to use
Claude for this experiment to reduce bias towards other models as no Anthropic models
are tested in the main experiments as they are currently not supported by RELRaE.

For each task (evaluation and refinement), we begin with an initial prompt. We refer
to this as a "Basic" prompt. We then proceed to refine the prompt by adding additional
features and reformatting the prompt as described by [2]. The stages of refinement
are as follows; clear instructions, assigning the LLM a role, and providing
domain context. For each prompt we test 5 different examples with the goal of evaluating
the consistency of the response quality. As the quality of a response is subjective,
we assess the quality of a response based on how well it would work within the context
of RELRaE.

#### Evaluation

| **Label** | **Domain** | **Range** | **Context** | **Expected Response** |
| ----- | ------ | ----- | ------- | ----------------- |
| hasSample | SampleSet | Sample | Analytical Chemistry | Yes |
| hasColour | Bird | Animal | Nature/Biology | No |
| isWrittenBy | Book | Publisher | General Knowledge | No |
| protects | Bodyguard | VIP | General Knowledge | Yes |
| partOf | HR Team | Company | Business | Yes |

| **Prompt Type** | **Prompt** |
| ------------- | -------- |
| Basic | "Does the label `x` accurately describe the relationship<br>between concepts `y` and `z`?" |
| Clear Instructions | "Within an ontology, does the label `x` accurately<br>describe the relationship between concepts<br>`y` and `z`? Give a 'Yes' or 'No' answer." |
| LLM Role | "You are a knowledge engineer building an ontology. Within<br>the ontology, does the label `x` accurately<br>describe the relationship between concepts `y` and<br>`z`? Give a 'Yes' or 'No' answer." |
| Domain Context | "You are a knowledge engineer building an ontology representing<br>the domain of `d`. Within the ontology, does the label<br>`x` accurately describe the relationship between concepts `y` and `z`?<br>Give a 'Yes' or 'No' answer." |

| **Prompt Type** | **Summary of Responses** | **Selected** |
| ------------- | ---------------------- | ---------- |
| Basic | | |
| Clear Instructions | | |
| LLM Role | | |
| Domain Context | | |

Full results can be found in `\preliminary_experiments\`

#### Refinement

| **Label** | **Domain** | **Range** | **Context** | **Example Expected Response** |
| ----- | ------ | ----- | ------- | ------------------------- |
| hasColour | Bird | Animal | Nature/Biology | isA |
| isWrittenBy | Book | Publisher | General Knowledge | publishedBy |
| learnsFrom | Teacher | Student | Education | teaches |
| locatedNear | Paris | France | Geography | locatedIn |
| hasPlant | Seed | Plant | Biology/Agriculture | growsInto |

| **Prompt Type** | **Prompt** |
| ------------- | -------- |
| Basic | "Considering the label `x` was rejected, refine the label describing<br>the relationship between concepts `y` and `z` so it<br>acurately describes the relationship between them." |
| Clear Instructions | "The label `x` was rejected for being an inaccurate representation<br>of the relationship between concepts `y` and `z` in an ontology.<br>Given this fact, refine the label `x` so that it is a<br>more accurate representation of the relationship. Do NOT repeat the given relationship." |
| LLM Role | "You are a knowledge engineer building an ontology. The label `x` was<br>rejected for being an inaccurate representation of the relationship between concepts<br>`y` and `z` in an ontology. Given this fact, refine the label `x` so that it is a<br>more accurate representation of the relationship. Do NOT repeat the given label." |
| Domain Context | "You are a knowledge engineer building an ontology representing the domain of `d`.<br>The label `x` wasrejected for being an inaccurate representation of the relationship between concepts<br>`y` and `z` in an ontology. Given this fact, refine the label `x` so that it is a<br>more accurate representation of the relationship. Do NOT repeat the given label." |

| **Prompt Type** | **Summary of Responses** | **Selected** |
| ------------- | ---------------------- | ---------- |
| Basic | | |
| Clear Instructions | | |
| LLM Role | | |
| Domain Context | | |

Full results can be found in `\preliminary_experiments\`

## Experiments

### 1.a Rules Set Comparison

### 1.b LLM Refinement Performance

### 2.a Value of Modules

### 2.b Quality of Ontology

## References

\[1\] Jingming Zhuo, Songyang Zhang, Xinyu Fang, Haodong Duan, Dahua Lin, and
  Kai Chen. 2024. ProSA: Assessing and Understanding the Prompt Sensitivity of LLMs.
  In Findings of the Association for Computational Linguistics: EMNLP 2024,
  pages 1950–1976, Miami, Florida, USA. Association for Computational Linguistics.

\[2\] Chen, B., Zhang, Z., Langrené, N., & Zhu, S. (2025). Unleashing the
  potential of prompt engineering for large language models. Patterns, 6(6).
