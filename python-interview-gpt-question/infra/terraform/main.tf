module "bigquery" {
  source      = "./modules/bigquery"
  project_id  = "terraform-tutorial-430708"
  dataset_id  = "ecommerce_data_raw"
  location    = "EU"
  description = "data for ecommerce platform"

  labels = {
    environment = "dev"
  }

  tables = {
    raw_sales_data = {
      schema      = file("schemas/raw_sales_data.json")
      description = "Raw sales data from ingestion."
    }
    customer_logs = {
      schema      = file("schemas/customer_logs.json")
      description = "Customer activity logs."
    }
    product_catalog = {
      schema      = file("schemas/product_catalog.json")
      description = "Product catalog details."
    }
  }
}

module "firestore" {
  source        = "./modules/firestore"
  project_id    = "terraform-tutorial-430708"
  database_name = "ecommerce-firestore"
  location_id   = "europe-west2"
}