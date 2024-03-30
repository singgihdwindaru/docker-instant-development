#https://devblogs.microsoft.com/dotnet/improving-multiplatform-container-support/
FROM --platform=$BUILDPLATFORM mcr.microsoft.com/dotnet/sdk:6.0-alpine AS debug
ARG TARGETARCH
ENV targetArch=$TARGETARCH

WORKDIR /source
COPY TodoApi/TodoApi.csproj .
RUN dotnet restore --runtime $targetArch

FROM debug AS publish
COPY TodoApi/. .
RUN dotnet publish --no-restore -c Release -o /app/publish

FROM mcr.microsoft.com/dotnet/aspnet:6.0-alpine as final
ENV ASPNETCORE_URLS http://*:8080

EXPOSE 8080
WORKDIR /app
COPY --from=publish /app/publish .
ENTRYPOINT ["./TodoApi"]