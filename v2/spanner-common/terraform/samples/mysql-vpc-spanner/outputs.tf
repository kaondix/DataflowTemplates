output "resource_ids" {
  description = "IDs of resources created during set up."
  value = {
    network          = google_compute_network.vpc_network.name
    subnetwork       = google_compute_subnetwork.vpc_subnetwork.name
    mysql_db_ip      = google_compute_instance.mysql_database_instance.network_interface[0].network_ip
    spanner_instance = google_spanner_instance.spanner_instance.name
  }
}

output "resource_urls" {
  description = "URLs of resources created during setup."
  value = {
    network          = "https://console.cloud.google.com/networking/networks/details/${google_compute_network.vpc_network.name}?project=${var.common_params.project}"
    subnetwork       = "https://console.cloud.google.com/networking/subnetworks/details/${var.common_params.region}/${google_compute_subnetwork.vpc_subnetwork.name}?project=${var.common_params.project}"
    mysql_db         = "https://console.cloud.google.com/compute/instancesDetail/zones/${var.mysql_params.zone}/instances/${google_compute_instance.mysql_database_instance.name}?project=${var.common_params.project}"
    spanner_instance = "https://console.cloud.google.com/spanner/instances/${google_spanner_instance.spanner_instance.name}/details/databases?project=${var.common_params.project}"
  }
  depends_on = [
    google_compute_network.vpc_network,
    google_compute_subnetwork.vpc_subnetwork,
    google_compute_instance.mysql_database_instance,
    google_spanner_instance.spanner_instance,
  ]
}