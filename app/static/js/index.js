async function ajax(url = "", data = {}) {
  const csrfToken = document.querySelector("[name=csrfmiddlewaretoken]").value;
  const response = await fetch(url, {
    method: "POST",
    credentials: "same-origin",
    headers: {
      "Content-Type": "application/json",
      "X-CSRFToken": csrfToken,
    },
    body: JSON.stringify(data),
  });
  return response.json();
}

const hotelColDefs = [
  {
    headerName: "ID",
    field: "id",
    width: 90,
    pinned: "left",
  },
  {
    headerName: "HotelName",
    field: "name",
    width: 300,
    pinned: "left",
  },
  {
    headerName: "Category",
    field: "category",
    width: 90,
    valueGetter: (params) => {
      return params.data.category ? params.data.category.name : "";
    },
  },
  {
    headerName: "Chain",
    field: "chain",
    width: 200,
    valueGetter: (params) => {
      return params.data.chain ? params.data.chain.name : "";
    },
  },
  {
    headerName: "Country",
    field: "area",
    width: 80,
    valueGetter: (params) => {
      return params.data.area ? params.data.area.region.country.code : "";
    },
  },
  {
    headerName: "Region",
    field: "area",
    width: 120,
    valueGetter: (params) => {
      return params.data.area ? params.data.area.region.name : "";
    },
  },
  {
    headerName: "Area",
    field: "area",
    width: 120,
    valueGetter: (params) => {
      return params.data.area ? params.data.area.name : "";
    },
  },
  {
    headerName: "Latitude",
    field: "latitude",
    width: 90,
  },
  {
    headerName: "Longitude",
    field: "longitude",
    width: 90,
  },
  {
    headerName: "Sales Contact",
    field: "sales_contact",
    width: 150,
    valueGetter: (params) => {
      return params.data.sales_contact ? params.data.sales_contact.email : "";
    },
  },
  {
    headerName: "Purchase Manager",
    field: "purchase_manager",
    width: 150,
    valueGetter: (params) => {
      return params.data.purchase_manager ? params.data.purchase_manager.user : "";
    },
  },
  {
    headerName: "Status",
    field: "status",
    width: 120,
    valueGetter: (params) => {
      return params.data.status ? params.data.status.name : "";
    },
    pinned: "right",
  },
  {
    headerName: "Giata",
    field: "giata",
    width: 90,
  },
  {
    headerName: "Tags",
    field: "tags", // Assuming 'tags' is the field name in your data
    valueGetter: (params) => {
      // Extract and concatenate tag names from the 'tags' array
      return params.data.tags
        .map((tag) => {
          return tag.name;
        })
        .join(", ");
    },
  },
];

const hotelGridOpts = {
  columnDefs: hotelColDefs,
  rowModelType: "serverSide",
  cacheBlockSize: 50,
  maxBlocksInCache: 2,
};

document.addEventListener("DOMContentLoaded", () => {
  const hotelGrid = document.querySelector("#hotel-grid");
  new agGrid.Grid(hotelGrid, hotelGridOpts);

  const dataSource = {
    getRows: (params) => {
      ajax("/api/hotel/", params.request)
        .then((response) => {
          params.successCallback(response, 30);
        })
        .catch((e) => {
          console.error(e);
          params.failCallback();
        });
    },
  };

  hotelGridOpts.api.setServerSideDatasource(dataSource);
});
