import pytest
from model_training_old import build_model_pipeline

def test_pipeline_creation():
    num_features = ["age","trestbps","chol"]
    cat_features = ["sex","cp"]
    pipeline = build_model_pipeline(num_features, cat_features)
    assert "preprocessor" in pipeline.named_steps
    assert "classifier" in pipeline.named_steps
    assert pipeline.named_steps["classifier"].n_estimators == 200